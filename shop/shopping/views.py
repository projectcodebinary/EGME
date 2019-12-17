from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from shopping.forms import RegisterForm
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse


def Home(request):
	return render(request, 'home.html', )

def SignUp(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'home.html')
	else:
		form = RegisterForm()
	return render(request, 'signup.html', {'form': form})

def Login(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			print("jvg")
			user = form.get_user()
			login(request, user)
			return render(request, 'home.html')
	else:
		form = AuthenticationForm()
	return render(request, 'login.html', {'form':form})

def Logout(request):
	if request.method == 'POST':
		logout(request)
		return render(request, 'home.html')


@login_required(login_url="Login/")
def ChangePassword(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			return redirect('../home')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'changepassword.html', {'form':form})


# Create your views here.







