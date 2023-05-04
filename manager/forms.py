from django import forms
from django.contrib.auth.models import User
from account.models import PostPay, Post


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='User name')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']


class PostPayUpdateForm(forms.ModelForm):
    paid = forms.BooleanField(required=False, label='完成繳費')

    class Meta:
        model = PostPay
        fields = ['paid']


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
