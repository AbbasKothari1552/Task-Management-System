from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth import get_user_model

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        UserModel = get_user_model()

        # Check if the email is already registered
        if UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
