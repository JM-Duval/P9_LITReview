from django.contrib.auth.forms import UserCreationForm # formulaire de creation
from django.contrib.auth.models import User # utilisateur
from django import forms  # formulaire

class CreateUser(UserCreationForm):
	class Meta:
		model=User
		fields=['username', 'password1', 'password2']

		