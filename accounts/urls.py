from django.urls import path
#from django.contrib.auth import views 
from . import views

app_name = 'accounts'

urlpatterns = [
	path('inscription', views.inscriptionPage, name='inscription'),
	#path('login', views.loginPage, name='login'),
	path('logout', views.logoutUser, name='logout'),
	path('home', views.home, name='home'),
]	