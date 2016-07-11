from django.shortcuts import render
from django.utils import timezone
from .models import Rooms
from .models import Timemodule

def login(request):
	return render(request, 'occupants/login.html', {})

def homepage(request):
	timeMod1 = Timemodule.objects.filter(room = "B-003")
	return render(request, 'occupants/homepage.html', {'timeMod1': timeMod1})
