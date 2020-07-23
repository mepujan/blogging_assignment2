from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Post

User = get_user_model()


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'address', 'DOB', 'mobile_number', 'profile_picture']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'blog']
