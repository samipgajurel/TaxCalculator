from django import forms
from .models import *


class NewsImageForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['headline','content','picture']
