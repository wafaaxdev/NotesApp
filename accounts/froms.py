from django import forms 
from .models import Profile
from django.contrib.auth.models import User



class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields =("headline","bio","img")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=("username","first_name","last_name","email")


