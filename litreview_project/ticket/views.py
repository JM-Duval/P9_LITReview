from django.shortcuts import render
from django.http import HttpResponse
#from .forms import createTicket
from django.forms import ModelForm
from .models import Contact 
from .models import Ticket


class TicketForm(ModelForm):
	class Meta:
		model = Ticket
		fields = ('title', 'user', 'image')

def ticket(request):
	ticket_form = TicketForm()
	return render(request, 'ticket/createticket.html', {'ticket_form': ticket_form})


class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ('name', 'firstname', 'email', 'message')

def contact(request):
	contact_form = ContactForm()
	return render(request, 'ticket/createticket.html', {'contact_form':contact_form})

"""


	def inscriptionPage(request):
	form=CreateUser()
	if request.method=='POST':
		form=CreateUser(request.POST)
		if form.is_valid():
			form.save()
			user=form.cleaned_data.get('username')
			messages.success(request, 'Compte créé avec succes pour '+ user)
			return redirect('accounts:login')
	context={'form': form}
	return render(request, 'accounts/inscription.html', context)

"""