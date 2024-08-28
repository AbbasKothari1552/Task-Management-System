from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
    path('',include('user.urls')),
    path('',include('taskmanager.urls')),

    path('accounts/', include('allauth.urls')),
]


