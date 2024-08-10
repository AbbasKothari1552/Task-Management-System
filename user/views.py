from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from allauth.account.views import SignupView, LoginView, LogoutView, ConfirmEmailView

from . forms import CustomSignupForm
from .serializers import CustomUserSerializer

# import logging

# logger = logging.getLogger(__name__)


# # Just for testing with postman
# @method_decorator(csrf_exempt, name='dispatch')
# class CustomSignupView(SignupView):
#     form_class = CustomSignupForm
#     # logger.info('Info message: Processing request')
#     def get_success_url(self):
#         # logger.debug('Debug message: Entered my_view')
#         # logger.info('Info message: Processing request')
#         return '/user/accounts/signup/'
    
#     def form_valid(self, form):
#         user = form.save(self.request)
#         return JsonResponse({
#             "status": "success",
#             "message": "User registered successfully."
#         })

#     def form_invalid(self, form):
#         # logger.warning('Warning message: This is just a warning')
#         # logger.critical('Critical message: Critical issue occurred')
#         return JsonResponse({
#             "status": "error",
#             "errors": form.errors
#         }, status=400)

class CustomSignupView(SignupView):
    form = CustomSignupForm

    def get_success_url(self):
        return reverse_lazy('account_login')
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form) -> HttpResponse:
        return super().form_invalid(form)

class CustomConfirmEmailView(ConfirmEmailView):
    def post(self, *args, **kwargs):
        response = super().post(*args, **kwargs)
        if self.get_user().is_authenticated:
            return redirect('/')
        return response

    def get_success_url(self):
        return reverse_lazy('/')

class CustomLoginView(LoginView):
    def get_success_url(self):
        # logger.debug("CustomLoginView get_success_url called")
        success_url = reverse_lazy('landingPage')
        print("Redirecting to:", success_url)
        return success_url

class CustomLogoutView(LogoutView):
    def get_next_page(self):
        # logger.debug("CustomLogoutView get_next_page called")
        return reverse_lazy('landingPage')  # Redirect to base URL