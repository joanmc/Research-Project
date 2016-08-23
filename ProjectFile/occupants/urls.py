from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^$', views.homepage, name='homepage'),
    url(r'^results/$', views.results, name= 'results'),
    url(r'^calendarGen$', views.calendarGen, name='calendarGen'),
    url(r'^GenGraph$', views.GenGraph, name='GenGraph'),
    url(r'^RoomDayGraph$', views.RoomDayGraph, name='RoomDayGraph'),
    url(r'^register/$', views.userFormView.as_view(), name='register'),
    url(r'^Rooms/$', login_required(views.SelectInfo), name='SelectInfo'),
    url(r'^Rooms/GTRequest$', views.GTRequest, name='GTRequest'),
    url(r'^Rooms/TMRequest$', views.TMRequest, name='TMRequest'),
    url(r'^Rooms/WFRequest$', views.WFRequest, name='WFRequest'),
    url(r'^wifilogs/$', views.wifilogs, name='wifilogs'),

   # Django Tutorial for Beginnners 30 Model Forms, thenewboston
    # Add records
    url(r'^Room/add/$', login_required(views.AddRoom.as_view()), name='AddRoom'),
    url(r'^Module/add/$', login_required(views.AddModule.as_view()), name='AddModule'),
    url(r'^TimeModule/add/$', login_required(views.AddTimeModule.as_view()), name='AddTimeModule'),
    url(r'^GroundTruth/add/$', login_required(views.AddGroundTruth.as_view()), name='AddGroundTruth'),
    # url(r'^Wifi/add/$', login_required(views.wifilogs), name='wifilogs'),
    # Update records
    url(r'^Room/(?P<pk>[a-zA-Z0-9()& ]+)/$', login_required(views.UpdateRoom.as_view()), name='UpdateRoom'),
    url(r'^Module/(?P<pk>[a-zA-Z0-9()& ]+)/$', login_required(views.UpdateModule.as_view()), name='UpdateModule'),
    url(r'^TimeModule/(?P<pk>[0-9]+)/$', login_required(views.UpdateTimeModule.as_view()), name='UpdateTimeModule'),
    url(r'^GroundTruth/(?P<pk>[0-9]+)/$', login_required(views.UpdateGroundTruth.as_view()), name='UpdateGroundTruth'),
    url(r'^Wifi/(?P<pk>[0-9]+)/$', login_required(views.UpdateWifi.as_view()), name='UpdateWifi'),
    # Delete records
    url(r'^Room/delete/(?P<pk>[a-zA-Z0-9()& ]+)/$', login_required(views.DeleteRoom.as_view()), name='DeleteRoom'),
    url(r'^Module/delete/(?P<pk>[a-zA-Z0-9()& ]+)/$', login_required(views.DeleteModule.as_view()), name='DeleteModule'),
    url(r'^TimeModule/delete/(?P<pk>[0-9]+)/$', login_required(views.DeleteTimeModule.as_view()), name='DeleteTimeModule'),
    url(r'^GroundTruth/delete/(?P<pk>[0-9]+)/$', login_required(views.DeleteGroundTruth.as_view()), name='DeleteGroundTruth'),
    url(r'^Wifi/delete/(?P<pk>[0-9]+)/$', login_required(views.DeleteWifi.as_view()), name='DeleteWifi'),

    # API 
    url(r'^RoomList/$', views.RoomList.as_view()),
    url(r'^ModuleList/$', views.ModuleList.as_view()),
    url(r'^GroundtruthList/$', views.GroundtruthList.as_view()),
    url(r'^TimemoduleList/$', views.TimemoduleList.as_view()),
    url(r'^BinaryPredictionsList/$', views.BinaryPredictionsList.as_view()),
    url(r'^PercentagePredictionsList/$', views.PercentagePredictionsList.as_view()),
    url(r'^EstimatePredictionsList/$', views.EstimatePredictionsList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

