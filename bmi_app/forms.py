from django import forms

class YourDataForm(forms.Form):
    weight = forms.IntegerField(label='体重(kg)')
    height = forms.IntegerField(label='身長(cm)')