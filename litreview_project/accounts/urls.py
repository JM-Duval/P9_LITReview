from django.urls import path
#from django.contrib.auth import views 
from . import views

app_name = 'accounts'

urlpatterns = [
	#path('login/', views.LoginView.as_view(), name="login"),
	#path('', views.index, name='index'),
	path('inscription', views.inscriptionPage, name='inscription'),
	path('login', views.loginPage, name='login'),
	path('logout', views.logoutUser, name='logout')
]	