from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Modules
from .models import Rooms
from .models import Timemodule
from django.db.models import Q
from datetime import timedelta, date
import datetime



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




def graphInfo(request):

	graphRoom = request.POST.get('graphRoom', False)
	graphDateTime = request.POST.get('graphDateTime', False)
	info = WiFiLogData.objects.filter(room = graphRoom.room, datetime__range=(graphDateTime, graphDateTime + timedelta(hours=1)))

	return render(request, 'occupants/homepage.html', {'info': info})



