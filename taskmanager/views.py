from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import TaskForm
from .models import Tag, Task
from .serializers import TagSerializer, TaskSerializer


@login_required
def task_list(request,date=None):
    date_str = request.GET.get('date')
    
    if date_str:
        # Parse the date from the string (format: YYYY-MM-DD)
        try:
            date = timezone.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            date = timezone.now().date()  # Fallback to current date on invalid date format
    else:
        date = timezone.now().date()  # Default to current date
    tasks = Task.objects.filter(user=request.user,date=date)
    serializer = TaskSerializer(tasks, many=True)
    form = TaskForm()
    return render(request, 'task.html', {'tasks': serializer.data, 'form':form})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
        else:
            return redirect('home')
    else:
        return redirect('task_list')

@login_required
def get_task(request,task_id):
    task = get_object_or_404(Task, id=task_id)
    # handling tag because of foreign key.
    tag = task.tag

    task_data = {
        'title' : task.title,
        'description' : task.description,
        # 'tag' : tag,
        'tag': { #not working.
            'id': task.tag.id,          # Include the tag ID
            'name': task.tag.name,      # Optionally include other tag fields
        },
        'priority' : task.priority,
        'date' : task.date,
        'time' : task.time,
        'repeat' : task.repeat
    }

    return JsonResponse(task_data)

@login_required
def edit_task(request,task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        else:
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    
    return redirect('task_list')

    
@login_required
def delete_task(request,task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    else:
        return redirect('task_list')







