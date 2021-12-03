from django import forms

class NameForm(forms.Form):
    name= forms.CharField(max_length=255)
    email= forms.CharField()
    subject=forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)