from django.urls import path
from . import views
from manager.views import (
    PostpayListView, 
    EditionListView,
    PostpayUpdateView,
    EditionCreateView,
    EditionUpdateView,
    PostnotpayListView,
    PostListView,
    UserListView,
    UserUpdateView,
    UserPostListView,
    PostUpdateView,
    CustomListView,
    CustomUpdateView
)
from account.views import PostDeleteView, PostPayDeleteView

urlpatterns = [
    path('manager_home',PostpayListView.as_view(), name='manager-home'),
    path('postpay/<int:pk>/',PostpayUpdateView.as_view(),name='postpay-detail'),
    path('edition/create',EditionCreateView.as_view(), name='edit-create'),
    path('edition/',EditionListView.as_view(), name='edit-list'),
    path('edition/update/<int:pk>/',EditionUpdateView.as_view(), name='edit-update'),
    path('postpay/notpay',PostnotpayListView.as_view(), name='notpay-list'),
    path('post',PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('postpay/<int:pk>/delete',
         PostPayDeleteView.as_view(), name='postpay-delete'),
    path('user_list',UserListView.as_view(), name='user-list'),
    path('user_detail/<int:pk>/',UserUpdateView.as_view(), name='user-detail'),
    path('user_post/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('custom',CustomListView.as_view(), name='custom-list'),
    path('custom/<int:pk>/',CustomUpdateView.as_view(),name='custom-update'),
]