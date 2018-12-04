from django import forms
from django.core import validators
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo
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
class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('url_site','profile_picture')
