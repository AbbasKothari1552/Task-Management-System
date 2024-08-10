from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
    path('', include('user.urls')),
    path('user/accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('user/accounts/login/', CustomLoginView.as_view(), name='account_login'),
    path('user/accounts/logout/', CustomLogoutView.as_view(), name='account_logout'),

    path('accounts/', include('allauth.urls')),
]
