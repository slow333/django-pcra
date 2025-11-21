from django.forms import ModelForm
from .models import IdolImage
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class IdolForm(ModelForm):
    title = forms.CharField(max_length=100)
    image = forms.ImageField()
    thumbnail = forms.ImageField(required=False)
    class Meta:
        model = IdolImage
        fields = ['title','image', 'thumbnail']

class IdolTitleForm(forms.Form):
    # label=False를 추가하여 이 필드의 레이블을 비활성화할 수 있습니다.
    title = forms.CharField(max_length=100, label=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False # 폼의 모든 레이블을 숨깁니다.
