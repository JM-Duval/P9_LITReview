from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TicketForm

def save_ticket(request, ticket_form):
	new_ticket =  ticket_form.save(commit=False)
	new_ticket.user = request.user
	new_ticket.save()

def ticket(request):
	ticket_form = TicketForm(request.POST, request.FILES)
	print(request.method)
	if request.method == 'POST':
		print('before to save')
		print(ticket_form)
		if ticket_form.is_valid():
			print('ticket valided')
			#save_ticket(request, ticket_form)
			new_ticket =  ticket_form.save(commit=False)
			new_ticket.user = request.user
			new_ticket.save()

			print('Ticket Saved')
			messages.success(request, 'Votre ticket à bien été enregistré')
			return redirect('/')
		else:
			ticket_form.errors

	return render(request, 'ticket/createticket.html', {'ticket_form': ticket_form})
