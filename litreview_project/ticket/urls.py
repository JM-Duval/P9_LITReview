from django.urls import path
#from django.contrib.auth import views 
from . import views

app_name = 'ticket'

urlpatterns = [
	path('ticket', views.contact, name='ticket'),
]	