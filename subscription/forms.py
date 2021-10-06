from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User
from django import forms 
from .models import UserFollows


class UserFollowsForm(ModelForm):
	class Meta:
		model = UserFollows
		fields = ['followed_user']
		labels = {'followed_user':"Nom d'utilisateur"}
		widgets = {
            'followed_user': TextInput(attrs={'class': 'form-control'}),
        }