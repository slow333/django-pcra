from django.forms import ModelForm
from .models import Image
from django import forms

class ImageForm(ModelForm):
    title = forms.CharField(max_length=100)
    image = forms.ImageField()
    thumbnail = forms.ImageField(required=False)
    class Meta:
        model = Image
        fields = ['title','image', 'thumbnail']
