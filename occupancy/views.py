from django.http import HttpResponse
from django.template import loader # to load templates

def index(resquest):
	#template = loader.get_template('occupancy/index.html')
	return HttpResponse("<h1>HOMEPAGE!!</h1>")
