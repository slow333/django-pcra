from django.shortcuts import render
from django.http import HttpResponse

def index(requst):
    return render(requst, 'index.html')

def contents(requst):
    return render(requst, 'contents.html')

def html_css(requst):
    return render(requst, 'others/html_css.html')

