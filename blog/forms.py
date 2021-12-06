from django import forms
from blog.models import Comment

class NameForm(forms.Form):
    name= forms.CharField(max_length=255)
    email= forms.CharField()
    subject=forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.ModelForm) :
    class Meta :
        model = Comment
        fields= ['post','name','email','subject','message']
