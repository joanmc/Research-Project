from django.conf.urls import url
from . import views

# Django Tutorial for Beginners - 5 - Views, thenewboston, YouTube
urlpatterns = [
    url(r'^$', views.index, name= 'index'),
]
