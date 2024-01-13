from django import forms
from django.utils.translation import gettext_lazy as _

class LoginForm(forms.Form):
    name = forms.CharField(label=_("Name or Email"),max_length=256)
    password = forms.CharField(label=_("Your Password"),widget=forms.PasswordInput)


