from django.urls import path
from . import views

# idol/
urlpatterns = [
    path('', views.blog_home, name='blog-home'),
    path('create/', views.blog_create, name='blog-create'),
    path('<int:pk>/update', views.blog_update, name='blog-update'),
    path('<int:pk>/delete', views.blog_delete, name='blog-delete'),
]
