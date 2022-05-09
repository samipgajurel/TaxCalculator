from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    phone = PhoneNumberField(help_text='Phone Number')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
'email', 'phone','password1', 'password2',)
