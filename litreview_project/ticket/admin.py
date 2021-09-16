from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
	list_display = ('title', 'description')

admin.site.register(Ticket, TicketAdmin)




