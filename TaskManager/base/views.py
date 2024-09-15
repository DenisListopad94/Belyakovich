from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def home(request):
    return HttpResponse("Welcome to our task management site")


def tasks(request):

    return render(request, 'tasks.html', get_tasks())


def users(request):
    users = [
        {"name": "John", "age": 25, "phone": "123-456-7890", 'photo': 'john.jpg'},
        {"name": "Alice", "age": 30, "phone": "987-654-3210", 'photo': 'static/john.jpg'},
        {"name": "Bob", "age": 28, "phone": "555-123-4567", 'photo': 'static/john.jpg'},
        {"name": "Eva", "age": 22, "phone": "666-888-9999", 'photo': 'static/john.jpg'}
    ]
    return render(request, 'users.html', {'users': users})


def get_tasks():
    context = {
        'all': Task.objects.all(),
        'h_priority': Task.objects.filter(priority='h'),
        'm_priority': Task.objects.filter(priority='m').exclude(status=''),
        'start_with': Task.objects.filter(title__startswith='Создать'),
    }
    return context
