from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from .models import shopping
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from django.contrib.auth.models import User
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm

cat=(
    ('order','Order'),('refund','Refund'),('delivery','Delivery'),('buying','Buying')
    )
class contact(forms.ModelForm):
    class Meta:
        model= shopping
        fields =('name','mail','phone','Query','section')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            'mail',
            'phone',
            'Query',
            'section',
            Submit('submit','Submit')
        )
    
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
))
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
