from django.conf.urls import url
from . import views


urlpatterns = [

    # url(r'^$',views.login, name='login'),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^calendarGen$', views.calendarGen, name='calendarGen'),
    url(r'^GenGraph$', views.GenGraph, name='GenGraph'),
    url(r'^RoomDayGraph$', views.RoomDayGraph, name='RoomDayGraph'),
    url(r'^register/$', views.userFormView.as_view(), name='register'),
    url(r'^Rooms/$', views.SelectInfo, name='SelectInfo'),
    url(r'^Stats/$', views.Stats, name= 'Stats'),

    # Django Tutorial for Beginnners 30 Model Forms, thenewboston
    # Add records
    url(r'^Room/add/$', views.AddRoom.as_view(), name='AddRoom'),
    url(r'^Module/add/$', views.AddModule.as_view(), name='AddModule'),
    url(r'^TimeModule/add/$', views.AddTimeModule.as_view(), name='AddTimeModule'),
    url(r'^GroundTruth/add/$', views.AddGroundTruth.as_view(), name='AddGroundTruth'),
    # Update records
    url(r'^Room/(?P<pk>[a-zA-Z0-9\-]+)/$', views.UpdateRoom.as_view(), name='UpdateRoom'),
    url(r'^Module/(?P<pk>[a-zA-Z0-9]+)/$', views.UpdateModule.as_view(), name='UpdateModule'),
    url(r'^TimeModule/(?P<pk>[0-9]+)/$', views.UpdateTimeModule.as_view(), name='UpdateTimeModule'),
    url(r'^GroundTruth/(?P<pk>[0-9]+)/$', views.UpdateGroundTruth.as_view(), name='UpdateGroundTruth'),
    # Delete records
    url(r'^Room/delete/(?P<pk>[a-zA-Z0-9\-]+)/$', views.DeleteRoom.as_view(), name='DeleteRoom'),
    url(r'^Module/delete/(?P<pk>[a-zA-Z0-9]+)/$', views.DeleteModule.as_view(), name='DeleteModule'),
    url(r'^TimeModule/delete/(?P<pk>[0-9]+)/$', views.DeleteTimeModule.as_view(), name='DeleteTimeModule'),
    url(r'^GroundTruth/delete/(?P<pk>[0-9]+)/$', views.DeleteGroundTruth.as_view(), name='DeleteGroundTruth'),
]
