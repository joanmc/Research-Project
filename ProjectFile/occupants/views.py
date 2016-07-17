from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from .models import Modules
from .models import Rooms
from .models import Timemodule
from .models import Wifilogdata
from django.db.models import Q
from datetime import timedelta, date
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
import json
from django.views.generic import View




def login(request):
    return render(request, 'occupants/login.html', {})



def homepage(request):

    if request.method == 'POST':

        b00X = request.POST.get('roomForm', False)
        start_time = datetime.date(2015, 11, 2)

        roomObj = Rooms.objects.filter(room = b00X)
        roomSchedule = Timemodule.objects.filter(room = b00X, datetime__range=(start_time, start_time + timedelta(days=5)))

        timeList = Timemodule.objects.filter(room = 'B-002', datetime__day= start_time.day)
        cleanTime = []
        for dt in timeList:
            cleanTime.append(dt.datetime.time)
        timeList = cleanTime

        roomList = Rooms.objects.all()
        moduleList = Modules.objects.all()

        return render(request, 'occupants/homepage.html', {'roomSchedule': roomSchedule, 'roomObj': roomObj, 'roomList': roomList, 'timeList': timeList, 'moduleList': moduleList})
	
    else:
        roomList = Rooms.objects.all()
        return render(request, 'occupants/homepage.html', {'roomList': roomList})



def test(request):

    if request.is_ajax():
        timeModuleId = request.POST['timeModuleId']
        
##        print("request: ", request)
##        print("data sent: ", timeModuleId)
        
        dateTime = Timemodule.objects.get(timemoduleid = timeModuleId)

        startTime = dateTime.datetime
        selectedRoom = dateTime.room.room
        
        wifiData = Wifilogdata.objects.filter(room = selectedRoom, datetime__range=(startTime, startTime + timedelta(hours=1)))

        authList =  []

        for x in wifiData:
##            print(x.room.capacity)
##            print(x.datetime)
##            print(x.authenticated)
            authList.append(x.authenticated)
 
        print("No of entries", len(authList))
        print("THE DATETIME", dateTime.datetime)
        print("THE DATETIME + 1 HOUR", dateTime.datetime + timedelta(hours=1))
        print("THE MODULE", dateTime.module.modulename)
        print("THE ROOM", dateTime.room.room)
        return HttpResponse(json.dumps(authList), content_type="application/json")

    else:
    	raise Http404




def test2(request):

    if request.is_ajax():
    	return HttpResponse('worked!')

    else:
    	raise Http404
