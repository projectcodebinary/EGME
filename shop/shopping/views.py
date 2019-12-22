from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from shopping.forms import RegisterForm,Additem
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMultiAlternatives 
from django.contrib import messages 
from django.core.mail import send_mail 
from django.template.loader import get_template 
from django.contrib.admin.views.decorators import staff_member_required
from .forms import Additem
from .models import additem
from django.shortcuts import render,get_object_or_404


def index(request):
	return render(request, 'index.html')

def Home(request):
	context = {}
	user_form = RegisterForm(request.POST)
	customer_form = AuthenticationForm(request.POST)
	Item=additem.objects.all()
	print(Item)
	context.update	({
		'user_form': user_form,
		'customer_form': customer_form,
		'Item': Item
	})
					
	return render(request, 'home.html',context )


def nav(request):
	Item=additem.objects.all()
	return render(request, 'nav.html', {'Item':Item})


def SignUp(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			message=('account created')
			emailvalue= form.cleaned_data.get("email")
			username = form.cleaned_data['username']
			# # print(emailvalue)
			# send_mail('Hello','Hello there, today i tried to add a email verification code','coolbinary69@gmail.com',
			# [emailvalue],
			# fail_silently=False)
			form.save()
			htmly = get_template('index.html')
			d = { 'username': username } 
			subject, from_email, to = 'welcome', 'coolbinary69@gmail.com', emailvalue  
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text / html")
			msg.send()
			messages.success(request, f'Your account has been created ! You are now able to log in') 

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
	return render(request, 'home.html')

@login_required(login_url="../Login/")
def ChangePassword(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			return redirect('../home')
	else:
		form = PasswordChangeForm(request.user)
	return render(request,'password.html', {'form':form})

# Create your views here.

def nav(request):
	Item=additem.objects.all()
	return render(request, 'nav.html', {'Item':Item})

@staff_member_required
def addditem(request):
	if request.method == "POST":
		form=Additem(request.POST, request.FILES)
		if form.is_valid():
			print('jdbab')
			form.save()
	form=Additem()
	return render(request,'additem.html',{'form':form})

# @login_required(login_url="../Login/")
def details(request,items):
	Item=get_object_or_404(additem,pk=items)
	return render(request, 'details.html', {'Item':Item})