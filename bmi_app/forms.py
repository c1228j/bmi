from django import forms
from django.core.exceptions import ValidationError

def check_zero(value):
    if value == 0:
        raise ValidationError("0以外の数字を入力してください")

class YourDataForm(forms.Form):
    weight = forms.IntegerField(label='体重(kg)')
    height = forms.IntegerField(label='身長(cm)', validators=[check_zero])
