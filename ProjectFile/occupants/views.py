from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Rooms
from .models import Timemodule
from django.db.models import Q
import datetime


def login(request):
	return render(request, 'occupants/login.html', {})


def homepage(request):
	
	if request.method == 'POST':	

		start_time = datetime.date(2015, 11, 1)
		end_time = datetime.date(2015, 11, 7)
	
		roomList = Rooms.objects.all()
		b00X = request.POST.get('roomForm', False)	
		b00Y = Timemodule.objects.filter(room= b00X, datetime__range=(start_time, end_time))
		var_time = [9,10,11,12,13,14,15,16,17]	

		return render(request, 'occupants/homepage.html', {'b00Y': b00Y, 'b00X': b00X, 'var_time': var_time, 'roomList': roomList})
	
	else:
		roomList = Rooms.objects.all()

		return render(request, 'occupants/homepage.html', {'roomList': roomList})



def setRoom(request):

	answer = request.POST['roomDropdown']
	b00X = Timemodule.objects.filter(room = answer, datetime__range=(start_time, end_time))
	
	var_time = [9,10,11,12,13,14,15,16,17]	

	return render(request, 'occupants/homepage.html', {'b00X': b00X, 'var_time': var_time, 'roomList': roomList})


