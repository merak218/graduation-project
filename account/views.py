from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView, 
    UpdateView, 
    DeleteView,
    )
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import (Profile, Post, PostPay, Customized,Edition)
from django.urls import reverse

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'account/home.html', context)

def customized(request):
    context = {
        'customs': Customized.objects.all()
    }
    return render(request, 'account/customized.html', context)

def choose_edition(request):
    context = {
        'edits':Edition.objects.all()
    }
    return render(request,'account/choose_model.html', context)

def payment(request):
    context = {
        'pays':PostPay.objects.all()
    }
    if request.POST:
        act_name = request.POST['title']
        edition = request.POST['edition']
        PostPay.objects.create(
            act_name =act_name,
            edition = edition
        )
    return render(request, 'account/payment.html', context)

class PaymentListView(ListView):
    model = PostPay
    template_name = 'account/payment.html'
    context_object_name='pays'
    ordering = ['paid']
    paginate_by = 10

class PostListView(ListView):
    model = Post
    template_name = 'account/home.html'
    context_object_name='posts'
    ordering = ['date_post']
    paginate_by = 10

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [  'title', 
                'date_post',
                'edition',
                'video_url', 
                'mar_text', 
                'image', 
                'content', 
                'qrcode'
            ]

    def form_vaild(self, form):
        form.instance.author = self.request.user
        return super.form_vaild(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/manager/manager_home'

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_superuser:
            return True
        return False

class UserPostListView(ListView):
    model = Post
    template_name = 'account/user_posts.html'
    context_object_name='posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('date_post')
    
    def get_success_url(self):
        username = self.kwargs['username']
        return reverse('user-posts', kwargs={'username': username})

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [  'title', 
                'date_post', 
                'edition',
                'video_url', 
                'mar_text', 
                'image', 
                'content', 
                'qrcode'
            ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save()
        return super().form_valid(form)

class CustomizedCreateView(LoginRequiredMixin, CreateView):
    model = Customized
    fields = [  'field',
                'date',
                'charge',
                'note',
            ]

    def form_valid(self, form):
        form.instance.contact = self.request.user
        self.object = form.save()
        return super().form_valid(form)

class CustomizedListView(ListView):
    model = Customized
    template_name = 'account/customized_list.html'
    context_object_name='customs'
    paginate_by = 10


class CustomizedDetailView(DetailView):
    model = Customized
    template_name = 'account/customized_detail.html'

class PostPayDeleteView(DeleteView):
    model = PostPay
    success_url = '/manager/manager_home'

    def test_func(self):
        postpay = self.get_object()
        if self.request.user.is_superuser:
            return True
        return False

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'your account has been updated !')
            return redirect('account:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'title':'Profile',
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'account/profile.html',context)