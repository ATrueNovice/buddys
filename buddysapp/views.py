from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from buddysapp.forms import UserForm, DispensaryForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return redirect(dispensary_home)

@login_required(login_url='/dispensary/sign-in/')
def dispensary_home(request):
    return render(request, 'dispensary/home.html')

def dispensary_sign_up(request):
    user_form = UserForm()
    dispensary_form = DispensaryForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        dispensary_form = DispensaryForm(request.POST, request.FILES)

        if user_form.is_valid() and dispensary_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_dispensary = dispensary_form.save(commit=False)
            new_dispensary.user = new_user
            new_dispensary.save()

            login(request, authenticate(
            username = user_form.cleaned_data["username"],
            password = user_form.cleaned_data["password"]
            ))

            return redirect(dispensary_home)

    return render(request, 'dispensary/signup.html', {
    "user_form": user_form,
    "dispensary_form": dispensary_form
    })
