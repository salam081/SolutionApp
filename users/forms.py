from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name','username', 'email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email',]


    
class ProfileUpdateForm(forms.ModelForm):
        
    class Meta:
        model = Profile
        fields = ['image']
        
