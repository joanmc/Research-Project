from django.shortcuts import render

def homepage (request):
	return render(request, 'occupants/homepage.html', {})

def test_page(request):
	return render(request, 'occupants/test_page.html', {})
