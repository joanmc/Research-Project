from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.utils import timezone
from django.template import loader
from .models import Modules, Groundtruth, Rooms, Timemodule, Wifilogdata, PercentagePredictions, EstimatePredictions
from django.db.models import Q
from datetime import timedelta, date
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
import json
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.serializers.json import DjangoJSONEncoder ## allow datetime format to serialize to json
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login as auth_login, authenticate #authenticates User & creates session ID
from .forms import userForm #Import user registration form
from chartit import DataPool, Chart


def login(request):
    return render(request, 'occupants/login.html', {})



def homepage(request):

        roomList = Rooms.objects.all()
        return render(request, 'occupants/homepage.html', {'roomList': roomList})


def calendarGen(request):
    '''function to query data for graph generation'''

    if request.method == 'POST':

        selectedRoom = request.POST.get('roomForm', False)
        startTime = request.POST.get('dateForm', False)
        startMonth = int(startTime[:2])
        startDay = int(startTime[3:5])
        startYear = int(startTime[6:])
        start_time = datetime.date(startYear, startMonth, startDay)
        roomObj = Rooms.objects.get(room=selectedRoom)
##        print('roomObj', roomObj.room)
        roomSchedule = Timemodule.objects.filter(room=selectedRoom,
                                                 datetime__range=(start_time, start_time + timedelta(days=5)))
        timeList = Timemodule.objects.filter(room=selectedRoom, datetime__day=start_time.day)
        calendarInfo = {"room": {"roomName": roomObj.room, "capacity": roomObj.capacity, "campus": roomObj.campus,
                                 "building": roomObj.building}, "times": [], "timeSlots": []}

        for dt in timeList:
##            print('datetime', dt.datetime.time())
            calendarInfo["times"].append({"time": dt.datetime.time()})

        for ts in roomSchedule:
            calendarInfo["timeSlots"].append({"date": ts.datetime.date(), "time": ts.datetime.time(),
                                              "moduleName": ts.module.modulename, "timeModuleId": ts.timemoduleid})

        return HttpResponse(json.dumps(calendarInfo, cls=DjangoJSONEncoder), content_type="application/json")
    else:
        raise Http404




def GenGraph(request):
    ''' function to query database for hourly graph data '''

    if request.is_ajax():

        timeModuleId = request.POST['timeModuleId']
        ##print('POST', timeModuleId) ## test ajax POST data has been recieved

        ## use POST data to query database and parse reutrn into required format
        timeModule = Timemodule.objects.get(timemoduleid = timeModuleId)
        startTime = timeModule.datetime
        selectedRoom = timeModule.room.room

        wifiData = Wifilogdata.objects.filter(room=selectedRoom,
                                              datetime__range=(startTime, startTime + timedelta(hours=1)))
        ##print('WIFI DATA', len(wifiData)) ## test number of returns from query
        predictions = EstimatePredictions.objects.get(room=selectedRoom, datetime=startTime)
        ## need error handling here for when no ground truth exists
        ##print('PREDICTION', len(prediction)) ## test number of returns from query

        groundTruthObj = Groundtruth.objects.get(room=selectedRoom, datetime=startTime)
        ## need error handling here for when no ground truth exists

        groundTruth = groundTruthObj.percentageestimate
        registered = timeModule.module.numreg
        capacity = timeModule.room.capacity
        predictionRange = predictions.predictions

        predictionUpper = int(predictionRange[predictionRange.index('-')+1:])
        predictionLower = int(predictionRange[:predictionRange.index('-')])

        ## test for variables
        ##print('GROUND TRUTH', groundTruth)
        ##print('REGISTERED', registered)
        ##print('CAPACITY', capacity)
        print('PREDICTION', predictionUpper, ':', predictionLower)

        jsonFile = {"timeSlice": [], "groundTruth": groundTruth, "registered": registered, "capacity": capacity,
                    "predictionLower": predictionLower, "predictionUpper": predictionUpper}

        for ts in wifiData:
            associated = ts.associated
            jsonFile["timeSlice"].append({'associated': associated})

        return HttpResponse(json.dumps(jsonFile), content_type="application/json")

    else:
        raise Http404




def RoomDayGraph(request):
    ''' function to query database for daily room graph data '''

    if request.is_ajax():

        selectedRoom = request.POST['selectedRoom']
##        print('POST', selectedRoom)
        selectedDate = request.POST['selectedDate']
##        print('POST', selectedDate)
        selectedYear = int(selectedDate[:4])
        selectedMonth = int(selectedDate[5:7])
        selectedDay = int(selectedDate[8:])
##        print('DATE', selectedDay, selectedMonth, selectedYear)
        selectedDateTime = date(selectedYear, selectedMonth, selectedDay)
        timeModuleList = Timemodule.objects.filter(room=selectedRoom,
                                                   datetime__range=(selectedDateTime,
                                                                    selectedDateTime + timedelta(days=1)))
        print('timeModuleList', len(timeModuleList))
        predictionList = PercentagePredictions.objects.filter(room=selectedRoom,
                                                              datetime__range=(selectedDateTime,
                                                                               selectedDateTime + timedelta(days=1)))
        print('predictionList', len(predictionList))
        groundTruthList = Groundtruth.objects.filter(room=selectedRoom,
                                                     datetime__range=(selectedDateTime,
                                                                      selectedDateTime + timedelta(days=1)))
        print('groundTruthList', len(groundTruthList))
        roomObj = Rooms.objects.get(room=selectedRoom)

        jsonFile = {"timeSlice": [], "capacity": roomObj.capacity}

        for i in range(0, len(timeModuleList)-1):
            time = timeModuleList[i].datetime.time()
            module = timeModuleList[i].module.modulename
            registered = timeModuleList[i].module.numreg
            prediction = predictionList[i].predictions
            groundTruth = groundTruthList[i].percentageestimate

            jsonFile["timeSlice"].append({'time': time, 'module': module, 'registered': registered,
                                          'prediction': prediction, 'groundTruth': groundTruth})

        return HttpResponse(json.dumps(jsonFile, cls=DjangoJSONEncoder), content_type = "application/json")
    else:
        raise Http404

def Stats(request):
    roomsList = Rooms.objects.all()
    rooms = []
    for room in roomsList:
        rooms.append(room)
    
    return render(request, 'occupants/Stats.html', {'rooms': rooms})



def SelectInfo(request):
    rooms = Rooms.objects.all()
    modules = Modules.objects.all()
    timemodule = Timemodule.objects.all()
    groundtruth = Groundtruth.objects.all()
    template = loader.get_template('occupants/forms.html')
    context = {
        'rooms': rooms,
        'modules': modules,
        'timemodule':timemodule,
        'groundtruth':groundtruth,
    }
    return HttpResponse(template.render(context, request))


class AddModule(CreateView):
    model = Modules
    fields = ['modulename', 'numreg']
    success_url = reverse_lazy('SelectInfo')

class AddRoom(CreateView):
    model = Rooms
    fields = ['room', 'building', 'campus', 'capacity']
    success_url = reverse_lazy('SelectInfo')

class AddTimeModule(CreateView):
    model = Timemodule
    fields = ['datetime', 'room', 'module', 'timemoduleid']
    success_url = reverse_lazy('SelectInfo')

class AddGroundTruth(CreateView):
    model = Groundtruth
    fields = ['datetime','room', 'binaryestimate', 'percentageestimate', 'groundtruthid']
    success_url = reverse_lazy('SelectInfo')

class UpdateModule(UpdateView):
    model = Modules
    fields = ['modulename', 'numreg']
    success_url = reverse_lazy('SelectInfo')

class UpdateRoom(UpdateView):
    model = Rooms
    fields = ['room', 'building', 'campus', 'capacity']
    success_url = reverse_lazy('SelectInfo')

class UpdateTimeModule(UpdateView):
    model = Timemodule
    fields = ['datetime', 'room', 'module', 'timemoduleid']
    success_url = reverse_lazy('SelectInfo')

class UpdateGroundTruth(UpdateView):
    model = Groundtruth
    fields = ['datetime','room', 'binaryestimate', 'percentageestimate', 'groundtruthid']
    success_url = reverse_lazy('SelectInfo')

class DeleteModule(DeleteView):
    model = Modules
    fields = ['modulename', 'numreg']
    success_url = reverse_lazy('SelectInfo')

class DeleteRoom(DeleteView):
    model = Rooms
    fields = ['room', 'building', 'campus', 'capacity']
    success_url = reverse_lazy('SelectInfo')

class DeleteTimeModule(DeleteView):
    model = Timemodule
    fields = ['datetime', 'room', 'module', 'timemoduleid']
    success_url = reverse_lazy('SelectInfo')

class DeleteGroundTruth(DeleteView):
    model = Groundtruth
    fields = ['datetime','room', 'binaryestimate', 'percentageestimate', 'groundtruthid']
    success_url = reverse_lazy('SelectInfo')


class userFormView(View):
    form_class = userForm #blueprint for form
    template_name = 'occupants/registration_form.html' #name of template to redirect to

    def get(self, request): #If user request is GET (display empty form) call this function
        form = self.form_class(None) #Specify what form we use
        return render(request, self.template_name, { 'form' : form })

    def post(self, request): #If user request is POST (submitting form) call this function
        form = self.form_class(request.POST)


        if form.is_valid():

            user = form.save(commit=False) #Doesn't save user yet. Customsing form below

            # standardise form inputs so they are clean and generic for our DB
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #Changing users password
            user.set_password(password)
            user.is_active = False #Change default. User is not active until admin grants permission
            user.save()

            #returns user objects if credentials are correct
            user = authenticate(username = username, password= password)

            if user is not None: 

                if user.is_active: #Checks if user hasnt been banned
                    auth_login(request, user)
                    return redirect('homepage')

        return render(request, self.template_name, { 'form' : form })
