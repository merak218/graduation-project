from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from .models import Edition
from account.models import Post, PostPay, Profile, Customized
from django.http import HttpResponseRedirect, request
from django.views.generic import (View, ListView,DetailView,CreateView, UpdateView, DeleteView)
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserUpdateForm , PostPayUpdateForm
from django.contrib import messages
from django.urls import reverse
# from manager.forms import PostpayUpdateForm
# from django.contrib import messages

def home(request):
    context = {
        'pays': PostPay.objects.all()
    }
    return render(request,'manager/home.html',context)

def edition_list(request):
    context = {
        'editions':Edition.objects.all()
    }
    return render(request, 'manager/edition_list.html', context)

def post_list(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'manager/post_list.html', context)

def user_list(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'manager/user_list.html', context)

def custom(request):
    context = {
        'customs': Customized.objects.all()
    }
    return render(request, 'manager/custom_list.html', context)

class EditionListView(ListView):
    model = Edition
    context_object_name='editions'
    template_name = 'manager/edition_list.html'
    paginate_by = 10

class EditionCreateView(LoginRequiredMixin, CreateView):
    model = Edition
    fields = ['edit_name', 'edit_img', 'charge']
    template_name = 'manager/edition_create.html'

    def form_vaild(self, form):
        self.object = form.save()
        return super.form_vaild(form)


class EditionUpdateView(LoginRequiredMixin, UpdateView):
    model = Edition
    fields = ['edit_name', 'edit_img', 'charge']
    template_name = 'manager/edition_update.html'

    def form_vaild(self, form):
        return super.form_vaild(form)

class PostpayListView(ListView):
    model = PostPay
    template_name = 'manager/home.html'
    context_object_name='pays'
    ordering = ['paid']
    paginate_by = 10

class PostnotpayListView(ListView):
    model = PostPay
    template_name = 'manager/notpay_list.html'
    context_object_name='pays'
    paginate_by = 10

class PostpayUpdateView(LoginRequiredMixin, UpdateView):
    model = PostPay
    form_class = PostPayUpdateForm
    # fields = [ 'paid' ]
    template_name = 'manager/postpay_detail.html'

    def form_vaild(self, form):
        return super.form_vaild(form)

    def get_success_url(self):
        return reverse('manager:notpay-list')

class PostListView(ListView):
    model = Post
    template_name = 'manager/post_list.html'
    context_object_name='posts'
    ordering = ['date_post']
    paginate_by = 10

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title',
              'date_post',
              'edition',
              'video_url',
              'mar_text',
              'image',
              'content',
              'qrcode'
              ]
    template_name = 'manager/post_detail.html'

    def form_vaild(self, form):
        return super.form_vaild(form)

    def get_success_url(self):
        return reverse('manager:post-list')

class UserListView(ListView):
    model = User
    template_name = 'manager/user_list.html'
    context_object_name='users'
    paginate_by = 10

class UserUpdateView(UpdateView):
    model = User
    fields = [ 'username', 'first_name', 'email' ]
    template_name = 'manager/user_detail.html'

    def form_vaild(self, form):
        return super.form_vaild(form)

    def get_success_url(self):
        user_id = self.kwargs['pk']
        return reverse('manager:user-detail', kwargs={'pk':user_id})

class UserPostListView(ListView):
    model = Post
    template_name = 'manager/user_posts.html'
    context_object_name='posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('date_post')
    
    def get_success_url(self):
        username = self.kwargs['username']
        return reverse('user-posts', kwargs={'username': username})

class CustomUpdateView(LoginRequiredMixin, UpdateView):
    model = Customized
    fields = [ 'contact', 'field', 'date', 'charge', 'note' ]
    template_name = 'manager/custom_update.html'

    def form_vaild(self, form):
        return super.form_vaild(form)

    def get_success_url(self):
        return reverse('manager:custom-list')

class CustomListView(ListView):
    model = Customized
    template_name = 'manager/custom_list.html'
    context_object_name='customs'
    paginate_by = 10