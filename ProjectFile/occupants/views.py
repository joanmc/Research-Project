from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Rooms
from .models import Timemodule
from .models import Modules
from django.db.models import Q
import datetime
from datetime import timedelta



def login(request):
	return render(request, 'occupants/login.html', {})



def homepage(request):
	
	if request.method == 'POST':	

##		timeList = Timemodule.objects.filter(room= 'B-002').values('datetime').distinct()
		start_time = datetime.date(2015, 11, 2)
		end_time = start_time + timedelta(days=5)
		
		moduleList = Modules.objects.all()
		roomList = Rooms.objects.all()
		b00X = request.POST.get('roomForm', False)
		roomObj = Rooms.objects.filter(room= b00X)
		roomSchedule = Timemodule.objects.filter(room= b00X, datetime__range=(start_time, end_time))
		var_time = [9,10,11,12,13,14,15,16,17]	

		return render(request, 'occupants/homepage.html', {'roomSchedule': roomSchedule, 'roomObj': roomObj, 'var_time': var_time, 'roomList': roomList})
	
	else:
		roomList = Rooms.objects.all()
		return render(request, 'occupants/homepage.html', {'roomList': roomList})



def setRoom(request):

	answer = request.POST['roomDropdown']
	b00X = Timemodule.objects.filter(room = answer, datetime__range=(start_time, end_time))
	
	var_time = [9,10,11,12,13,14,15,16,17]	

	return render(request, 'occupants/homepage.html', {'b00X': b00X, 'var_time': var_time, 'roomList': roomList})


