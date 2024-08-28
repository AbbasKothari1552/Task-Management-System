from django.urls import path
from .views import *

urlpatterns = [
    path('task/', task_list, name='task_list'),
    path('add_task/', add_task, name='add_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('get_task/<int:task_id>/', get_task, name='get_task'),
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),
]