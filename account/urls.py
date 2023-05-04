from django.urls import path
from django.conf.urls import url
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    UserPostListView,
    PaymentListView,
    CustomizedCreateView,
    CustomizedDetailView,
    CustomizedListView
    )
from account import views as user_views

urlpatterns = [
    path('user_home/', PostListView.as_view(), name='user-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('payments/', PaymentListView.as_view(), name='user-payments'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('profile/', user_views.profile, name='profile'),
    path('choose/', user_views.choose_edition, name='choose'),
    path('customized_create/', CustomizedCreateView.as_view(), name='customized-create'),
    path('customized/<int:pk>/', CustomizedDetailView.as_view(), name='customized-detail'),
    path('customized/', CustomizedListView.as_view(), name='customized-list'),
]