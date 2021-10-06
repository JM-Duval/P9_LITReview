from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUser


def home(request):
	"""Home page. Connexion or inscription is possible"""
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			messages.info(request, "Utilisateur et mot de passe incorrects	")
	return render(request, 'accounts/home.html')


def inscription_page(request):
	"""Needed : user name and passeword (form)"""
	form = CreateUser()
	if request.method == 'POST':
		form = CreateUser(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Compte créé avec succes pour '+ user)
			return redirect('accounts:home')
	context = {'form': form}
	return render(request, 'accounts/inscription.html', context)


def logout_user(request):
	"""function for desconnetion"""
	logout(request)
	return redirect('accounts:login')
