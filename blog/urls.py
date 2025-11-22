from django.urls import path
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    UserPostListView
    )

# idol/
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('', views.blog_home, name='blog-home'),
    # path('create/', views.blog_create, name='post-create'),
    # path('<int:pk>/update', views.blog_update, name='post-update'),
    # path('<int:pk>/delete', views.blog_delete, name='post-delete'),
]
# class view를 사용하면
# app / model_viewtype.html , blog/post_list.html