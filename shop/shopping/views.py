from django.shortcuts import render,get_object_or_404
from .models import shopping
from django.http import HttpResponse
from .forms import contact,RegisterForm,AuthenticationForm
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm,PasswordChangeForm
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def shopping(request):
	if request.method == 'POST':
		form= contact(request.POST)
		if form.is_valid():
			print("Valid")
			form.save()
	form = contact()
	return render(request,'home.html',{'form':form})



def SignUp(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'login.html')
	else:
		form = RegisterForm()
	return render(request, 'signup.html', {'form': form})

def index(request):
	return render(request,'index.html')


def Login(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return render(request, 'home.html')
	else:
		form = AuthenticationForm()
	return render(request, 'login.html', {'form':form})

def Logout(request):
	if request.method == 'POST':
		logout(request)
		print("khbds")
		# messages.info(request, "Logged out successfully!")
		return render(request, 'home.html')

@login_required(login_url="/Login")
def ChangePassword(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			return redirect('home.html')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'passwordchange.html', {'form':form})

