from django.urls import path
from . import views


app_name = 'subscription'

urlpatterns = [
	path('subscription', views.subscription, name='subscription'),
	path('unsubscribe/<int:followed_user_id>', views.unsubscribe, name='unsubscribe'),
]	
