from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to our task management site")


def tasks(request):
    tasks = [
        {'task': 'task 1', 'status': 'started', 'category': 'work'},
        {'task': 'task 2', 'status': 'started', 'category': 'personal'},
        {'task': 'task 3', 'status': 'completed', 'category': 'work'},
        {'task': 'task 4', 'status': 'pending', 'category': 'personal'},
        {'task': 'task 5', 'status': 'started', 'category': 'work'},
    ]
    return render(request, 'tasks.html', {'tasks': tasks})


def users(request):
    users = [
        {"name": "John", "age": 25, "phone": "123-456-7890", 'photo': 'john.jpg'},
        {"name": "Alice", "age": 30, "phone": "987-654-3210", 'photo': 'static/john.jpg'},
        {"name": "Bob", "age": 28, "phone": "555-123-4567", 'photo': 'static/john.jpg'},
        {"name": "Eva", "age": 22, "phone": "666-888-9999", 'photo': 'static/john.jpg'}
    ]
    return render(request, 'users.html', {'users': users})
