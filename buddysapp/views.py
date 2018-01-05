from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return redirect(dispensary_home)

@login_required(login_url='/dispensary/sign-in/')
def dispensary_home(request):
    return render(request, 'dispensary/home.html', {})

def dispensary_sign_up(request):
    return render(request, 'dispensary/signup.html', {})
