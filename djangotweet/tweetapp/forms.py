from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet

class AddTweetForm(forms.Form): 
    nickname = forms.CharField(label="Nickname", max_length=100)
    message = forms.CharField(label="Message", widget=forms.Textarea)

class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ["username","message"]