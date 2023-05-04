# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserResgisterForm
import account


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.user.is_authenticated():
        if request.user.is_superuser():
            return HttpResponseRedirect('manager/manager_home/')
        else:
            return HttpResponseRedirect('user/user_home')
    else:
        return HttpResponseRedirect('/home')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)


def register(request):
    if request.method == 'POST':
        form = UserResgisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'your account has been created ! you are now able to login !')
            return redirect('login')
    else:
        form = UserResgisterForm()
    return render(request, 'register.html', {'form': form})

