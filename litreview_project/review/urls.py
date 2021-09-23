from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('review/', views.review, name='review'),
	path('review/<int:ticket_id>/', views.review, name='review'),
	
]	

 

