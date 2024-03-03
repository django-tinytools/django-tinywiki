from django import forms
from django.utils.translation import gettext_lazy as _

class LoginForm(forms.Form):
    name = forms.CharField(label=_("Name or Email"),max_length=256)
    password = forms.CharField(label=_("Your Password"),widget=forms.PasswordInput)

class SignupForm(forms.Form):
    username = forms.CharField(label=_("Name"),max_length=64)
    email = forms.EmailField(label=_("Email"))
    first_name = forms.CharField(label=_("First Name"),max_length=64,required=False)
    last_name = forms.CharField(label=_("Last Name"),max_length=64,required=False)
    password0 = forms.CharField(label=_("Password"),widget=forms.PasswordInput())
    password1 = forms.CharField(label=_("Confirm Password"),widget=forms.PasswordInput())
