from django import forms
from .models import Rooms, Modules


class addRoom(forms.ModelForm):
	
	class Meta:
		model = Rooms
		fields = ('room', 'building', 'campus', 'capacity',)


class addModule(forms.ModelForm):
	
	class Meta:
		model = Modules
		fields = ('modulename', 'numreg',)


