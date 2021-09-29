from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TicketForm

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
