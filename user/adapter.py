from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model

import logging
logger = logging.getLogger(__name__)

class CustomAccountAdapter(DefaultAccountAdapter):

    def confirm_email(self, request, email_address):
        user = email_address.user
        user.email_verified = True # Mark email as verified
        user.save()
        super().confirm_email(request, email_address)
    
    def get_login_redirect_url(self, request):
        # Override this method to customize where users are redirected after login
        path = "/home/"
        return path

# class MySocialAccountAdapter(DefaultSocialAccountAdapter):
#     def post_social_login(self, request, sociallogin):
#         user = sociallogin.user
#         print("Inside")
#         if user.is_authenticated:
#             # Example: Toggle a custom email field or perform any email-related action
#             if user.email and not user.email_verified:
#                 # Update email verification status or send verification email
#                 print("Yes user email is verified")
#                 user.email_verified = True
#                 user.save()


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        # Automatically set is_email_verified to True for social logins
        user.email_verified = True
        user.save()
        return user