from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from user.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль',
        'id': 'password',   
        'name':'password',  
        'autocomplete':'on',  
        'minlength': '8',
        'maxlength': '16',
        'bpattern':'[0-9a-fA-F]{8,16}'         
    }))
    class Meta:
        model = User
        fields = ('username', 'password')
        

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Придумайте имя пользователя',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Введите адрес эл. почты',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Придумайте пароль',
        'id': 'password',   
        'name':'password',  
        'autocomplete':'on',  
        'minlength': '8',
        'maxlength': '16',
        'bpattern':'[0-9a-fA-F]{8,16}'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Подтвердите пароль',
        'id': 'password',   
        'name':'password',  
        'autocomplete':'on',  
        'minlength': '8',
        'maxlength': '16',
        'bpattern':'[0-9a-fA-F]{8,16}'
    }))
    class Meta: 
        model = User
        fields = ('username', 'email', 'password1', 'password2') 

        