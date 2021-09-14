from django.shortcuts import render
from .models import Projet

def index(request):
	projet = Projet.objects.all()
	#return render(request, 'review/index.html', {'projet':projet})
	return render(request, 'review/index.html', {'projet':projet})
	#return render(request, 'review/index.html', {'projet':projet})
	#return render(request, 'review/index.html', {'projet':projet})
	#return render(request, 'review/index.html', {'projet':projet})
