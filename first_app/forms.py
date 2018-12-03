from django import forms
from django.core import validators
class formName(forms.Form):
    name=forms.CharField()
    email=forms.CharField()
    email_again=forms.CharField(label='Please enter your Email again')
    text=forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['email_again']
        if email != vemail:
            raise forms.ValidationError("Make sure your Email matches")