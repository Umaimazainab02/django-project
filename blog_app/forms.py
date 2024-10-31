from django import forms
from .models import Add_Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Add_Blog
        fields = ["title", "image"]
        
        
        
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        
        fields = ("username", "email", "password1", "password2")