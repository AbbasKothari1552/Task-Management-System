from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Tag, Task
from .serializers import TagSerializer, TaskSerializer

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return render(request, 'task.html', {'tasks': serializer.data})



@login_required
@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        # redirect to task_list view
        return redirect('task_list')
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





