from django import forms
from django.contrib.auth.models import User
from .models import additem,sizes,adress
from django.contrib.auth.forms import UserCreationForm
from verified_email_field.forms import VerifiedEmailField
from django.forms import ModelForm



class Additem(forms.ModelForm):
    class Meta:
        model=additem
        fields = '__all__'
     
        
class changesize(forms.ModelForm):
    class Meta:
        model= sizes
        fields='__all__'
        

class address(forms.ModelForm):
    class Meta:
        model=adress
        fields=['add','name','pincode','locality','street','landmark','city','state']
        widgets = { 
            'add': forms.Textarea(attrs={'placeholder': 'ADDRESS','class': "fuk"}),
            'name': forms.Textarea(attrs={'placeholder': 'YOUR NAME','class': "fuk"}),
            'pincode': forms.Textarea(attrs={'placeholder': 'PINCODE','class': "fuk"}),
            'locality': forms.Textarea(attrs={'placeholder': 'LOCALITY','class': "fuk"}),
            'landmark': forms.Textarea(attrs={'placeholder': 'LANDMARK','class': "fuk"}),
            'street': forms.Textarea(attrs={'placeholder': 'STREET','class': "fuk"}),
            'city': forms.Textarea(attrs={'placeholder': 'CITY','class': "fuk"}),
            'state': forms.Textarea(attrs={'placeholder': 'STATE','class': "fuk"}),
        } 



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

      def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Account already exists with this email. Please use different or try LOGIN')
        return email