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
from .forms import Additem,changesize
from .models import additem,sizes
from django.shortcuts import render,get_object_or_404
from .models import Order
from .models import Profile
from django.urls import reverse
from .models import OrderItem, Order,sizes

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


# def nav(request):
# 	Item=additem.objects.all()
# 	return render(request, 'nav.html', {'Item':Item})


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
	return render(request,'changepassword.html', {'form':form})

# Create your views here.

def nav(request):
	# users=Profile.objects.filter(user=request.user).first()
	# size= sizes.objects.all()
	form=changesize(request.POST)
	size='M'
	if form.is_valid():
		size=form.cleaned_data['size']
		form.save()
	Item=additem.objects.filter(size=size)
	
	context={
		'Item':Item,
		'form':form,
	}
	return render(request, 'nav.html', context)


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






def my_profile(request):
	my_user_profile = Profile.objects.filter(user=request.user).first()
	my_orders = Order.objects.filter(is_ordered=True, owner = my_user_profile)
	context = {
		'my_orders': my_orders
	}
	return render(request, "profile.html", context)

@login_required(login_url="../Login/")
def product_list(request):
	object_list = additem.objects.all()
	filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
	current_order_products = []
	if filtered_orders.exists():
		user_order = filtered_orders[0]
		user_order_items = user_order.items.all()
		current_order_products = [product.product for product in user_order_items]

	context = {
		'object_list': object_list,
		'current_order_products': current_order_products
	}

	return render(request, "product_list.html", context)






@login_required(login_url="../Login/")
def add_to_cart(request, **kwargs):
	user_profile = get_object_or_404(Profile, user=request.user)
	product = additem.objects.filter(id=kwargs.get('item_id', "")).first()
	if product in request.user.profile.items.all():
		messages.info(request, 'You already own this ebook')
		return redirect(reverse('product-list'))
	order_item, status = OrderItem.objects.get_or_create(product=product)
	user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
	user_order.items.add(order_item)
	if status:
		user_order.save()
	messages.info(request, "item added to cart")
	return redirect(reverse('nav'))




@login_required(login_url="../Login/")
def delete_from_cart(request, item_id):
	item_to_delete = OrderItem.objects.filter(pk=item_id)
	if item_to_delete.exists():
		item_to_delete[0].delete()
		messages.info(request, "Item has been deleted")
	return redirect(reverse('order_summary'))



def get_user_pending_order(request):
	# get order for the correct user
	user_profile = get_object_or_404(Profile, user=request.user)
	order = Order.objects.filter(owner=user_profile, is_ordered=False)
	if order.exists():
		# get the only order in the list of filtered orders
		return order[0]
	return 0

@login_required(login_url="../Login/")
def order_details(request, **kwargs):
	user_profile = get_object_or_404(Profile, user=request.user)
	existing_order = get_user_pending_order(request)
	things= Order.objects.filter(owner=user_profile, is_ordered=False)
	context = {
		'order': existing_order,
		'things':things
	}
	return render(request, 'order_summary.html', context)



# def changesizes(request):
# 	if request.method == 'POST':
# 		form = changesize(request.POST)
# 		t=sizes.objects.get(pk=1)
# 		if form.is_valid():
# 			same=form.cleaned_data['size']
# 			t.size=same
# 			t.save()
# 			return redirect('../nav')
# 	else:
# 		form = changesize()
# 	return render(request,'nav.html', {'form':form})



