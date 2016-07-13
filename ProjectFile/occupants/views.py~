from django.shortcuts import render
from django.utils import timezone
from .models import Rooms
from .models import Timemodule
from django.db.models import Q
import datetime

def login(request):
	return render(request, 'occupants/login.html', {})

def homepage(request):
	start_time = datetime.date(2015, 11, 1)
	end_time = datetime.date(2015, 11, 7)

	timeMod1 = Timemodule.objects.filter(room='B-004', datetime__range=(start_time, end_time))
	
	var_time = [9,10,11,12,13,14,15,16,17]	

	return render(request, 'occupants/homepage.html', {'timeMod1': timeMod1, 'var_time': var_time})
