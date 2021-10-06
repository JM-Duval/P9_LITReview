from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import UserFollowsForm
from .models import UserFollows


def subscription(request):
	User = get_user_model()
	users = User.objects.all().exclude(username = request.user)
	userfollows = UserFollows.objects.all()
	subscripters = []
	subscriptions = []
	for user in userfollows:
		if user.followed_user.id == request.user.id:
			subscripters.append(user.user.id)
		if user.user.id == request.user.id:
			subscriptions.append(user.followed_user)
	userfollows_form = UserFollowsForm(request.POST)
	if request.method == 'POST':
		userfollows_form = UserFollowsForm(request.POST)
		if userfollows_form.is_valid():
			userfollows = userfollows_form.save(commit=False)
			userfollows.user = request.user
			userfollows.save()
			print('saved !')
			return redirect('/subscription')
	return render(request, 'subscription/subscription.html', 
		{'userfollows_form':userfollows_form,'users':users,'subscripters':subscripters,
		'subscriptions':subscriptions})


def unsubscribe(request, followed_user_id):
	user = request.user
	followers = UserFollows.objects.all()
	for follower in followers:
		if follower.user.id == user.id:
			if follower.followed_user.id == followed_user_id:
				print(f'{follower.user} ne suivit plus {follower.followed_user}')
				instance = follower
				instance.delete()
	return redirect('/subscription')
