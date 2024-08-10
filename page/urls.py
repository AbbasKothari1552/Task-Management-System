from django.urls import path
from . import views

urlpatterns = [
    path('', views.basePage, name='basePage'),
    path('home/', views.home, name='home'),
]