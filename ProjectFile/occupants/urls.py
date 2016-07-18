from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$',views.login, name='login'),
    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^graphGen$', views.graphGen, name='graphGen'),
    url(r'^test$', views.test, name='test'),
]
