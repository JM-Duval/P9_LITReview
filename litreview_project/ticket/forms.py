from django.forms import ModelForm
from django.contrib.auth.models import User # utilisateur
from django import forms  # formulaire
from .models import Ticket

"""
class CreateTicket(ModelForm):
    class Meta:
        model = Ticket
        fields = ["titre", "description", "user"]
        

        widgets = {
            'titre': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'})
        }

"""


"""
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'})
        }

from django import forms

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)

"""