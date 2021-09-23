from django.contrib import admin
#from .models import Projet
from .models import Review

"""
class ProjetAdmin(admin.ModelAdmin):
	list_display = ('titre', 'description')

admin.site.register(Projet, ProjetAdmin)
"""

class ReviewAdmin(admin.ModelAdmin):
	list_display = ('ticket','rating', 'headline', 'body', 'user', 'time_created')

admin.site.register(Review, ReviewAdmin)