from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main-home'),
    path('docs/', views.contents, name='contents'),
]