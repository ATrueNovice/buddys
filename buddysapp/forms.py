from django import forms

from django.contrib.auth.models import User
from buddysapp.models import Dispensary, Product

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")

class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

class DispensaryForm(forms.ModelForm):
    class Meta:
        model = Dispensary
        fields = ("name", "address", "phone", "logo")

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("dispensary",)
