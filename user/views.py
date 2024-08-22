from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from allauth.account.views import SignupView, LoginView, LogoutView, ConfirmEmailView

from . forms import CustomSignupForm
from .serializers import CustomUserSerializer

