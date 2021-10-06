from itertools import chain
from django.shortcuts import render, redirect
from django.db.models import CharField, Value
from ticket.forms import TicketForm
from ticket.models import Ticket
from ticket.views import save_ticket
from .forms import ReviewForm
from .models import Review


def index(request):
    tickets = Ticket.objects.all()
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = Review.objects.all()
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    user = request.user
    if tickets.count():
        if reviews.count():
            free_tickets = tickets.exclude(response=True)
            posts = sorted(chain(reviews, free_tickets), key=lambda 
            post: post.time_created, reverse=True)
            return render(request, 'review/index.html', 
                context={'posts':posts,'user':user})
        else:
            posts = sorted(chain(reviews, tickets), key=lambda 
                post: post.time_created, reverse=True)
            return render(request, 'review/index.html', 
                context={'posts':posts,'user':user})
    else:
        return render(request, 'review/index.html', {'tickets':tickets,
                                                     'reviews':reviews,})
    

def save_review(request, review_form, ticket):  
    new_review =  review_form.save(commit=False)
    new_review.user = request.user
    new_review.ticket = ticket
    new_review.save()
 
 
def review(request, ticket_id=None):
    """2 possibilities : create review from ticket or without ticket"""
    if ticket_id is None: # Create ticket & review
        ticket_form = TicketForm(request.POST, request.FILES) 
        review_form = ReviewForm(request.POST)
        if request.method == 'POST':
            save_ticket(request, ticket_form)
            ticket = Ticket.objects.last()
            ticket.response = True
            ticket.save()
            save_review(request, review_form, ticket)
            return redirect('/')
        return render(request, 'review/askreview.html', 
            {'review_form': review_form, 'ticket_form': ticket_form})
    else: # reply to ticket
        ticket = Ticket.objects.get(id__exact=ticket_id)
        review_form = ReviewForm(request.POST)
        status = 'reply'
        if request.method == 'POST':
            save_review(request, review_form, ticket)
            ticket.response = True
            ticket.save()
            return redirect('/')
        return render(request, 'review/replyreview.html', 
            {'review_form': review_form,'ticket': ticket,'status': status})


def modify_review(request, review_id):
    review = Review.objects.get(id__exact=review_id)
    ticket = review.ticket
    user = request.user
    review_form = ReviewForm(instance=review)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review.save()
            return redirect('/')
    return render(request, 'review/modifyreview.html', 
        {'review_form':review_form,'ticket':ticket,'user':user})


def delete_review(request, review_id):
    review = Review.objects.get(id__exact=review_id)
    ticket = review.ticket
    review.delete()
    ticket.delete()
    return redirect('/')


def modify_ticket_in_review(request, ticket_id):
    ticket = Ticket.objects.get(id__exact=ticket_id)
    ticket_form = TicketForm(instance=ticket)
    reviews = Review.objects.all()
    for review in reviews:
        if review.ticket == ticket:
            review_form = ReviewForm(instance=review)
            if request.method == 'POST':
                review_form = ReviewForm(request.POST, instance=review)
                ticket_form = TicketForm(request.POST, request.FILES, 
                    instance=ticket)
                if ticket_form.is_valid():
                    ticket.save()
                if review_form.is_valid():
                    review.save()
                return redirect('/posts')
    return render(request, 'review/modifyticketinreview.html', 
        {'ticket_form':ticket_form, 'ticket':ticket})
