import sqlite3
from sqlite3 import Error
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Task, CompletedTask


def edit_task(request):
    task_id = request.GET.get('id') 
    title = request.GET.get('task')
    description = request.GET.get('description')
    date = request.GET.get('date')
    
    if title and date:
        tasks = Task.objects.filter(task_id=task_id)
        for task in tasks:
            task.task_title = title
            task.task_description = description
            task.task_date = date
            task.save()

        tasks = Task.objects.all()
        return render(request, 'home/edit_task.html', context={'tasks': tasks})

    else:
        messages.error(request, 'Erro! Confira as informações.')
        return render(request, 'home/create_task.html')


def conclude_task(request, task_id):
    Task.objects.filter(task_id=task_id).delete()
    CompletedTask.objects.create(completed_task_id=task_id)

    tasks = CompletedTask.objects.all()
    return render(request, 'home/index.html', context={'tasks': tasks})


def delete_task(request, task_id):
    Task.objects.filter(task_id=task_id).delete()    
    tasks = Task.objects.all()
    return render(request, 'home/index.html', context={'tasks': tasks})


def create_task(request):   
    return render(request, 'home/create_task.html')


def validate_form(request):
    task = request.GET.get('task')
    description = request.GET.get('description')
    date = request.GET.get('date')
    
    if task and date:
        Task.objects.create(task_title=task, task_description=description, task_date=date)
        tasks = Task.objects.all().order_by('task_date')
        return render(request, 'home/index.html', context={'tasks': tasks})

    else:
        messages.error(request, 'Erro! Confira as informações.')
        return render(request, 'home/create_task.html')


def index(request):

    if request.GET.get('conclude'):
        conclude_task(request, request.GET.get('conclude'))
    
    if request.GET.get('edit'):
        tasks = Task.objects.filter(task_id=request.GET.get('edit'))
        return render(request, 'home/edit_task.html', context={'tasks': tasks})
    
    if request.GET.get('delete'):
        delete_task(request, request.GET.get('delete'))
        
    tasks = Task.objects.all().order_by('task_date')
    return render(request, 'home/index.html', context={'tasks': tasks})


