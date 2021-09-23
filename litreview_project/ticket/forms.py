from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User # utilisateur
from django import forms  # formulaire
from .models import Ticket

class TicketForm(ModelForm):
	class Meta:
		model = Ticket
		fields = ['title', 'description', 'image']
		widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
        }