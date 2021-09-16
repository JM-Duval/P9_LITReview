from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import ModelForm
from .models import Ticket
from django.contrib import messages

 
class TicketForm(ModelForm):
	class Meta:
		model = Ticket
		fields = ['title', 'description', 'image']


def ticket(request):
	ticket_form = TicketForm(request.POST, request.FILES)
	print(request.FILES)
	if request.method == 'POST':
		#ticket_form= TicketForm(request.POST)
		ticket = ticket_form.save(commit=False)
		ticket.user = request.user
		ticket.save()
		messages.success(request, 'Votre ticket à bien été enregistré')
		return redirect('/')

		#if ticket_form.is_valid():
		#	ticket_form.save()
			#ticket = form.cleaned_data.get('title')
		#	messages.success(request, 'Votre ticket à bien été enregistré')
		#	return redirect('/')
	return render(request, 'ticket/createticket.html', {'ticket_form': ticket_form})


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