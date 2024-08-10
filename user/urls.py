from django.urls import path
from .views import CustomSignupView,CustomLoginView,CustomLogoutView, CustomConfirmEmailView

urlpatterns = [
    # path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    # path('accounts/confirm-email/', CustomConfirmEmailView.as_view(), name='account_confirm_email'),
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='account_logout'),
]