from django.shortcuts import render
from .models import Review, Projet
from ticket.models import Ticket
from django.forms import ModelForm


def index(request):
	ticket = Ticket.objects.all()
	return render(request, 'review/index.html', {'ticket':ticket})


	#projet = Projet.objects.all()
	#return render(request, 'review/index.html', {'projet':projet})

 
class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = ('ticket', 'rating', 'headline', 'body', 'user')


def review(request):
	review_form = ReviewForm()
	return render(request, 'review/createreview.html', {'review_form': review_form})


