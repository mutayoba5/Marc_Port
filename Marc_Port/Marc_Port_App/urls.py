from django.conf.urls import url
from Marc_Port_App import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
