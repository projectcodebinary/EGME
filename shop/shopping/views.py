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
from .forms import Additem,changesize,address
from .models import additem,sizes
from django.shortcuts import render,get_object_or_404
from .models import Order
from .models import Profile
from django.urls import reverse
from .models import OrderItem, Order,sizes
from .models import delivery,adress,Transaction,ordered
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .number import number
from django.contrib.auth.models import User
from .extras import generate_order_id, transact, generate_client_token

import datetime
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


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
		
	context={
		'form':form,
	}
	return render(request, 'signup.html',context)


def Login(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			print("jvg")
			user = form.get_user()
			login(request, user)
			return HttpResponseRedirect('../nav')
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

def changeaddr(request):
	usr=get_object_or_404(Profile, user=request.user)
	forms=address(request.POST)
	if request.method == 'POST':
		if forms.is_valid():
			windows=forms.cleaned_data['add']
			addd=forms.cleaned_data['add']
			pin=forms.cleaned_data['pincode']
			name=forms.cleaned_data['name']
			locality=forms.cleaned_data['locality']
			street=forms.cleaned_data['street']
			city=forms.cleaned_data['city']
			state=forms.cleaned_data['state']
			landmark=forms.cleaned_data['landmark']
			pn=adress.objects.filter(own=usr)
			pn.add=addd
			pn.pincode=pin
			pn.name=name
			pn.locality=locality
			pn.city=city
			pn.state=state
			pn.landmark=landmark
			pn.street=street
				
			if adress.objects.filter(own=usr).all().count()==0:
				adress.objects.get_or_create(own = usr,add=addd,pincode=pin,city=city,state=state,street=street,locality=locality,landmark=landmark,name=name)
			pn.filter(own=usr).all().update(add=addd,pincode=pin,city=city,state=state,street=street,locality=locality,landmark=landmark,name=name)
	addon=adress.objects.filter(own=usr)
	return render(request,'changeaddress.html', {'forms':forms})


@login_required(login_url="../Login/")
def nav(request):
	win=address(request.POST)
	form=changesize(request.POST)
	size='M'
	if form.is_valid():
		size=form.cleaned_data['size']
		form.save()
	Item=additem.objects.filter(size=size)
	usr=get_object_or_404(Profile, user=request.user)
		

	if win.is_valid():

		windows=win.cleaned_data['add']
		addd=win.cleaned_data['add']
		pin=win.cleaned_data['pincode']
		name=win.cleaned_data['name']
		locality=win.cleaned_data['locality']
		street=win.cleaned_data['street']
		city=win.cleaned_data['city']
		state=win.cleaned_data['state']
		landmark=win.cleaned_data['landmark']
		pn=adress.objects.filter(own=usr)
		pn.add=addd
		pn.pincode=pin
		pn.name=name
		pn.locality=locality
		pn.city=city
		pn.state=state
		pn.landmark=landmark
		pn.street=street
		
		if adress.objects.filter(own=usr).all().count()==0:
			adress.objects.get_or_create(own = usr,add=addd,pincode=pin,city=city,state=state,street=street,locality=locality,landmark=landmark,name=name)
		pn.filter(own=usr).all().update(add=addd,pincode=pin,city=city,state=state,street=street,locality=locality,landmark=landmark,name=name)
	addon=adress.objects.filter(own=usr)
	context={
		'Item':Item,
		'form':form,
		'win':win,
		'addon':addon
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

@login_required(login_url="../Login/")
def details(request,items):
	usr=get_object_or_404(Profile, user=request.user)
	Item=get_object_or_404(additem,pk=items)
	adon = get_object_or_404(adress,own=usr)
	context={
		'Item':Item,
		'adon':adon
	}
	return render(request, 'details.html', context)



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
		messages.info(request, 'You already own this product')
		return redirect(reverse('order_summary'))
	order_item, status = OrderItem.objects.get_or_create(product=product)
	user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
	user_order.items.add(order_item)
	if status:
		user_order.save()
	messages.info(request, "item added to cart")
	return redirect(reverse('order_summary'))




@login_required(login_url="../Login/")
def delete_from_cart(request, item_id):
	item_to_delete = OrderItem.objects.filter(pk=item_id)
	if item_to_delete.exists():
		item_to_delete[0].delete()
		messages.info(request, "Item has been deleted")
	return redirect(reverse('order_summary'))



@login_required(login_url="../Login/")
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
	ping=get_object_or_404(delivery)
	adon = get_object_or_404(adress,own=user_profile)
	context = {
		'order': existing_order,
		'things':things,
		'ping':ping,
		'local':user_profile,
		'adon':adon,
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







@login_required()
def checkout(request, **kwargs):
    client_token = generate_client_token()
    existing_order = get_user_pending_order(request)
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        token = request.POST.get('stripeToken', False)
        if token:
            try:
                charge = stripe.Charge.create(
                    amount=100*existing_order.get_cart_total(),
                    currency='usd',
                    description='Example charge',
                    source=token,
                )

                return redirect(reverse('update_records',
                        kwargs={
                            'token': token
                        })
                    )
            except stripe.CardError as e:
                messages.info(request, "Your card has been declined.")
        else:
            result = transact({
                'amount': existing_order.get_cart_total(),
                'payment_method_nonce': request.POST['payment_method_nonce'],
                'options': {
                    "submit_for_settlement": True
                }
            })

            if result.is_success or result.transaction:
                return redirect(reverse('update_records',
                        kwargs={
                            'token': result.transaction.id
                        })
                    )
            else:
                for x in result.errors.deep_errors:
                    messages.info(request, x)
                return redirect(reverse('checkout'))
            
    context = {
        'order': existing_order,
        'client_token': client_token,
        'STRIPE_PUBLISHABLE_KEY': publishKey
    }

    return render(request, 'checkout.html', context)


@login_required()
def update_transaction_records(request, token):
    # get the order being processed
    order_to_purchase = get_user_pending_order(request)

    # update the placed order
    order_to_purchase.is_ordered=True
    order_to_purchase.date_ordered=datetime.datetime.now()
    order_to_purchase.save()
    
    # get all items in the order - generates a queryset
    order_items = order_to_purchase.items.all()

    # update order items
    order_items.update(is_ordered=True, date_ordered=datetime.datetime.now())

    # Add products to user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # get the products from the items
    order_products = [item.product for item in order_items]
    user_profile.ebooks.add(*order_products)
    user_profile.save()

    
    # create a transaction
    transaction = Transaction(profile=request.user.profile,
                            token=token,
                            order_id=order_to_purchase.id,
                            amount=order_to_purchase.get_cart_total(),
                            success=True)
    # save the transcation (otherwise doesn't exist)
    transaction.save()


    # send an email to the customer
    # look at tutorial on how to send emails with sendgrid
    messages.info(request, "Thank you! Your purchase was successful!")
    return redirect(reverse('my_profile'))


def success(request, **kwargs):
    # a view signifying the transcation was successful
    return render(request, 'purchase_success.html', {})





def cash(request):	
	usr=get_object_or_404(Profile, user=request.user)
	detail=Order.objects.filter(owner=usr)
	detail.is_ordered=True
	detail.ref_code=number
	detail.filter(owner=usr).all().update(is_ordered=True,ref_code=number)
	det=Order.objects.filter(owner=usr).filter(id=1)
	print(det)
	for items in det:
		# print(items.items.filter(id=1))
		ordered.it=det







	# emailvalue=ui
	# username=request.user.username
	# num=number
	# num.str()
	# htmly = 'Your order number is '+ number
	# d = { 'username': username } 
	# subject, from_email, to = 'welcome','coolbinary69@gmail.com', emailvalue  
	# html_content = htmly
	# msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
	# msg.attach_alternative(html_content, "text / html")
	# msg.send()
	return redirect(reverse('nav'))
