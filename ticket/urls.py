from django.urls import path
#from django.contrib.auth import views 
from . import views


app_name = 'ticket'

urlpatterns = [
	path('ticket', views.ticket, name='ticket'),
	path('modifyticket/<int:ticket_id>', views.modifyticket, name='modifyticket'),
	path('deleteticket/<int:ticket_id>', views.deleteticket, name='deleteticket'),
]	
