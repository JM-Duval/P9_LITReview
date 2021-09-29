from django import forms
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from ticket.models import Ticket
from ticket.views import save_ticket
from ticket.forms import TicketForm
from itertools import chain
from django.db.models import CharField, Value


def index(request):
    tickets = Ticket.objects.all()
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = Review.objects.all()
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    if tickets.count():
        if reviews.count():
            for review in reviews:
                #free_tickets = tickets.exclude(title=review.ticket.title)
                free_tickets = tickets.exclude(response=True)
            posts = sorted(chain(reviews, free_tickets), key=lambda post: post.time_created, reverse=True)
            return render(request, 'review/index.html', context={'posts':posts})
        else:
            posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)
            return render(request, 'review/index.html', context={'posts':posts})

    else:
        return render(request, 'review/index.html', {'tickets':tickets,
                                                     'reviews':reviews})
    

def save_review(request, review_form, ticket):  
    new_review =  review_form.save(commit=False)
    new_review.user = request.user
    new_review.ticket = ticket
    new_review.save()
 

def review(request, ticket_id=None):
    if ticket_id is None: # Create ticket & review
        ticket_form = TicketForm(request.POST, request.FILES) 
        review_form = ReviewForm(request.POST)
        if request.method == 'POST':
            print(ticket_form.instance)
            save_ticket(request, ticket_form)
            ticket = Ticket.objects.last()
            ticket.response = True
            ticket.save()
            save_review(request, review_form, ticket)
            return redirect('/')
        return render(request, 'review/askreview.html', {'review_form': review_form,
                                                         'ticket_form': ticket_form})
    
    else: # reply to ticket
        ticket = Ticket.objects.get(id__exact=ticket_id)
        review_form = ReviewForm(request.POST)
        if request.method == 'POST':
            save_review(request, review_form, ticket)
            ticket.response = True
            ticket.save()
            return redirect('/')
        return render(request, 'review/replyreview.html', {'review_form': review_form,
                                                           'ticket': ticket})

def reviewss(request, ticket_id=None):
    review_form = ReviewForm(request.POST)
    if request.method == 'POST':
        review = review_form.save(commit=False)
        review.user = request.user
        review.ticket = 'ticket_test'
        review.save()
        return redirect('/')
    return render(request, 'review/createreview.html', {'review_form': review_form})

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