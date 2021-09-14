from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	#path('ticket', views.createTicket, name='ticket'),
	path('', views.index, name='index'),
]