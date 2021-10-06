from django.contrib import admin
#from .models import Ticket
from .views import UserFollows

class UserFollowsAdmin(admin.ModelAdmin):
	list_display = ('user','followed_user')

admin.site.register(UserFollows, UserFollowsAdmin)