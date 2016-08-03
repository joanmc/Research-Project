from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$',views.login, name='login'),
    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^calendarGen$', views.calendarGen, name='calendarGen'),
    url(r'^GenGraph$', views.GenGraph, name='GenGraph'),
    url(r'^RoomDayGraph$', views.RoomDayGraph, name='RoomDayGraph'),
]
