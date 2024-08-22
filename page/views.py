from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def basePage(request):
    return render(request, 'base.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

@login_required(login_url='')
def home(request):
    return render(request, 'home.html')
