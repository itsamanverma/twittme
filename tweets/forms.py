from django import forms

from .models import Tweet

MAX_TWEET_LENGTH = 200

class TweetFrom(forms.ModelForm):
    class Meta: 
        model = Tweet
        feild = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("this tweet is too long...")
        return content