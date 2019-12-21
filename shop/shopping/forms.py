from django import forms
from django.contrib.auth.models import User
from .models import additem
from django.contrib.auth.forms import UserCreationForm
from verified_email_field.forms import VerifiedEmailField
from django.forms import ModelForm



class Additem(forms.ModelForm):
    class Meta:
        model=additem
        fields = '__all__'
     
        

class AuthenticationForm(forms.Form):
      username= forms.CharField(widget=forms.TextInput(
          attrs={
            'class':'user',
            'placeholder': 'username',
            'padding':'5px',
    }
))
      password= forms.CharField(widget=forms.TextInput(
          attrs={
            'class':'user',
            'placeholder': 'username',
            'padding':'5px',
    }
))
      class Meta:
         model = User
         fields = ["username","password"]



class RegisterForm(UserCreationForm):
      email= forms.EmailField(widget=forms.TextInput(
          attrs={
            'class':'form-control',
            'placeholder': 'Email id',
            'padding': '10px'
    }
),label='email',required=True,)
      first_name=forms.CharField(widget=forms.TextInput(
          attrs={
            'class':'form-control',
            'placeholder': 'Your first name',
    }
))
      second_name= forms.CharField(widget=forms.TextInput(
          attrs={
            'class':'form-control',
            'placeholder': 'Your Second name',
    }
))

      password1= forms.CharField(widget=forms.TextInput(
          attrs={
            'class':'form-control',
            'placeholder': 'Enter Password',
    }
))    
      password2= forms.CharField(widget=forms.TextInput(
          attrs={
            'class':'form-control',
            'placeholder': 'Re-enter password',
    }
))
      username= forms.CharField(widget=forms.TextInput(
          attrs={
            'class':'form-control',
            'placeholder': 'Username',
            'onfocus': 'this.placeholder = '''
    }
))

      class Meta: 
         model = User
         fields = ["username", "email", "first_name", "second_name", "password1", "password2"]
