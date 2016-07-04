from django.conf.urls import url
from . import views

urlpatterns = [
    # Default homepage
    # Django Tutorial for Beginners-5-Views, thenewboston, YouTube
    url(r'^$', views.index, name='index'),

]
