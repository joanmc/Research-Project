from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$',views.homepage, name='homepage'),
    url(r'^test/$', views.test_page, name='test_page'),
]
