from django.shortcuts import render
from .models import Post
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
# Create your views here.

def home(requeset):
	Data = {'Posts': Post.objects.all().order_by('-date')}
	return render(requeset, 'pages/home.html', Data)

def post(requeset, id):
	postt = Post.objects.get(id=id)
	return render(requeset, 'pages/post.html',{'post':postt})

#def register(requeset):
#	form = RegistrationForm(requeset.POST)
#	if requeset.method == 'POST':
#		if form.is_valid():
#			form.save()
#			return HttpResponseRedirect('/')
#	return render(requeset, 'pages/register.html', {'form': form})

def login_views(requeset):
	if requeset.method == 'POST':
		user = None
		form = AuthenticationForm(data=requeset.POST)
		if form.is_valid():
			user = form.get_user()
			login(requeset, user)
			username = requeset.user.username
			requeset.session['username'] = username
			return HttpResponseRedirect('/motor')
	else:
		form = AuthenticationForm()
	return render(requeset, 'pages/login.html', {'form': form})

def logout_views(requeset):
	if requeset.method == 'POST':
		logout(requeset)
		return HttpResponseRedirect('/')
	return render(requeset, 'pages/logout.html')
