from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def confirm_email(self, request, email_address):
        user = email_address.user
        user.email_verified = True # Mark email as verified
        user.save()
        super().confirm_email(request, email_address)
    
    def get_login_redirect_url(self, request):
        # Override this method to customize where users are redirected after login
        path = "/custom-redirect/"
        return path