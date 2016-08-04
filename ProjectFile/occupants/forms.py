from django import forms
from .models import Rooms, Modules
from django.contrib.auth.models import User



class addRoom(forms.ModelForm):
	
	class Meta:
		model = Rooms
		fields = ('room', 'building', 'campus', 'capacity',)


class addModule(forms.ModelForm):
	
	class Meta:
		model = Modules
		fields = ('modulename', 'numreg',)


class userForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)


	class Meta:
		model = User
		fields = ['username', 'email' ,'password']
