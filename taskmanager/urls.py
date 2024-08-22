from django.urls import path
from .views import *

urlpatterns = [
    path('task/', task_list, name='task_list'),
]