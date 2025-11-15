from django.urls import path
from . import views

urlpatterns = [
    path('', views.contents, name='contents'),
    path('others/html-css', views.html_css, name='docs-html-css'),
]