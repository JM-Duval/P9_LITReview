from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
	path('inscription', views.inscription_page, name='inscription'),
	#path('login', views.loginPage, name='login'),
	path('logout', views.logout_user, name='logout'),
	path('home', views.home, name='home'),
]
