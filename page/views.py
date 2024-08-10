from django.shortcuts import render

def basePage(request):
    return render(request, 'base.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def home(request):
    return render(request, 'home.html')
