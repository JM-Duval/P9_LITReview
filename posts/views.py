from django.shortcuts import render, redirect
from django.contrib import messages
from ticket.models import Ticket
from review.models import Review
from itertools import chain
from django.db.models import CharField, Value


def posts (request):
	tickets = Ticket.objects.all()
	tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
	reviews = Review.objects.all()
	reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
	user = request.user

	tickets_user = []
	for ticket in tickets:
		if ticket.user == user :
			tickets_user.append(ticket)
		else:
			continue

	reviews_user = []
	for review in reviews:
		if review.user == user :
			reviews_user.append(review)
		else:
			continue

	posts = sorted(chain(reviews_user, tickets_user), key=lambda post: post.time_created, reverse=True)
	return render(request, 'posts/posts.html', context={'posts':posts,
														'user':user})




