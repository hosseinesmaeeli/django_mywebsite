from django import forms
from website.models import Contact, Newsletter

class NameForm(forms.Form):
    name= forms.CharField(max_length=255)
    email= forms.CharField()
    subject=forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm) :
    class Meta :
        model = Contact
        fields= '__all__'
        # fields=['name','email']

class NewsletterForm(forms.ModelForm)   :
    class Meta :
        model = Newsletter
        fields = '__all__'     