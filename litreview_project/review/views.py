from django import forms
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from ticket.models import Ticket
from ticket.views import save_ticket
from ticket.forms import TicketForm
from itertools import chain


def index(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    print(tickets)
    for review in reviews:
        free_tickets = tickets.exclude(title=review.ticket.title)
    print(free_tickets)
    posts = sorted(chain(reviews, free_tickets), key=lambda post: post.time_created, reverse=True)
    #return render(request, 'review/index.html', {'tickets':free_tickets,
    #                                             'reviews':reviews})
    return render(request, 'review/index.html', {'posts':posts})


def save_review(request, review_form):
    new_review =  review_form.save(commit=False)
    new_review.user = request.user
    new_review.save()

def review(request, ticket_id=None):
    if ticket_id == None:
        ticket_form = TicketForm(request.POST, request.FILES) 
        review_form = ReviewForm(request.POST)
        if request.method == 'POST':
            save_review(request, review_form)
            save_ticket(request, ticket_form)
            return redirect('/')
        return render(request, 'review/askreview.html', {'review_form': review_form,
                                                         'ticket_form': ticket_form})
    
    else:
        ticket_selected = Ticket.objects.get(id__exact=ticket_id)
        ticket = ticket_selected
        review_form = ReviewForm(request.POST)
        if request.method == 'POST':
            save_review(request, review_form)
            return redirect('/')
        return render(request, 'review/replyreview.html', {'review_form': review_form,
                                                           'ticket': ticket})



"""
def review(request):
    review_form = ReviewForm(request.POST)
    if request.method == 'POST':
        review = review_form.save(commit=False)
        review.user = request.user
        review.save()
        return redirect('/')
    return render(request, 'review/createreview.html', {'review_form': review_form})    

def askreview(request):
    review_form = ReviewForm(request.POST)
    ticket_form = TicketForm(request.POST, request.FILES)
    return render(request, 'review/askreview.html', {'review_form': review_form,
                                                     'ticket_form': ticket_form})

def createreview(request):
    #ticket_form = TicketForm(request.POST, request.FILES)
    ticket_form = ticket(request)
    review_form = ReviewForm(request.POST, request.FILES)
    return render(request, 'review/createreview.html', {'review_form': review_form,
                                                        'ticket_form': ticket_form})

"""