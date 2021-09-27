from django.shortcuts import render, redirect
#from .models import Projet
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUser
from django.contrib import messages


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

def loginPage(request):
	context={}
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		#else:
		#	messages.infos(request, "Utilisateur et mot de passe incorrects	")
	#return render(request, 'accounts:login', context)
	return render(request, 'accounts/login.html', context)


"""
def index(request):
	projet = Projet.objects.all()
	return render(request, 'review/index.html', {'projet':projet})
"""

def logoutUser(request):
	logout(request)
	return redirect('accounts:login')

