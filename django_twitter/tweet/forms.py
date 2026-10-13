from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
  class Meta:
    model = Tweet
    fields = ['text', 'image'] # here we are using array bcz we are using self  made forms

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2') #here we are storing in tuple bz we are using builtin forms

