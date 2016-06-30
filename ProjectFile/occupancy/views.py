from django.http import HttpResponse
# Django Tutorial for Beginners - 5 - Views, thenewboston, YouTube

def index(request):
	return HttpResponse("<H1> This is going to be the home page</h1>")
