from django.urls import path
from . import views


app_name = 'ticket'

urlpatterns = [
	path('ticket', views.ticket, name='ticket'),
	path('modifyticket/<int:ticket_id>', views.modify_ticket, name='modifyticket'),
	path('deleteticket/<int:ticket_id>', views.delete_ticket, name='deleteticket'),
]	
