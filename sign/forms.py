from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserResgisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='User name (使用者名稱)')
    class Meta:
        model = User
        fields = ['username','first_name','email','password1','password2']
        labels = {
            'username' : ('Account (使用者帳號)'),
        }