from django.forms import ModelForm, TextInput, Textarea, FileInput
from .models import Ticket


class TicketForm(ModelForm):
	class Meta:
		model = Ticket
		fields = ['title', 'description', 'image']
		widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'image': FileInput(attrs={'class': 'form-control'})
        }
