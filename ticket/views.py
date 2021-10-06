from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TicketForm
from .models import Ticket


def save_ticket(request, ticket_form):
	new_ticket =  ticket_form.save(commit=False)
	new_ticket.user = request.user
	new_ticket.save()

 
def ticket(request):
	ticket_form = TicketForm(request.POST, request.FILES)
	if request.method == 'POST':
		if ticket_form.is_valid():
			save_ticket(request, ticket_form)
			messages.success(request, 'Votre ticket à bien été enregistré')
			return redirect('/')
		else:
			ticket_form.errors

	return render(request, 'ticket/createticket.html', {'ticket_form': ticket_form})


def modify_ticket(request, ticket_id):
	ticket = Ticket.objects.get(id__exact=ticket_id)
	ticket_form = TicketForm(instance=ticket)
	if request.method == 'POST':
		ticket_form = TicketForm(request.POST, request.FILES, instance=ticket)
		if ticket_form.is_valid():
			ticket.save()
			return redirect('/posts')
	return render(request, 'ticket/modifyticket.html', {'ticket_form':ticket_form,
														'ticket':ticket})


def delete_ticket(request, ticket_id):
	ticket = Ticket.objects.get(id__exact=ticket_id)
	ticket.delete()
	return redirect('/')
