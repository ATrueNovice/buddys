from django import forms

from django.contrib.auth.models import User
from buddysapp.models import Dispensary

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")

class DispensaryForm(forms.ModelForm):
    class Meta:
        model = Dispensary
        fields = ("name", "address", "phone", "logo")
