from django.urls import path
from . import views

urlpatterns = [
    path('', views.idol_home, name='idol-home'),
    path('upload/', views.upload, name='idol-upload'),
    path('<int:pk>/detail', views.detail, name='idol-detail'),
    path('<int:pk>/delete', views.delete, name='idol-delete'),
]
