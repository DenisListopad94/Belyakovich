from django.shortcuts import render
from django.http import HttpResponse

from .forms import TaskForm, CommentForm
from .models import Task, User, Comment


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


# Homework 4
def show_tasks(request):
    context = {
        'task_with_tags': Task.objects.filter(tags__isnull=False),
        'task_without_users': Task.objects.filter(user=None),
        'users_older_30': User.objects.filter(age__gt=30, locale=None),
        'comments_with_id': Comment.objects.filter(user_id__in=[1, 4, 5]),
    }
    return render(request, 'home_work.html', context=context)


def new_task(request):
    context = {}
    form = TaskForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'new_task.html', context)


# def add_comment(request):
#     context = {}
#     form = CommentForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#
#         form.save()
#     context['form'] = form
#     return render(request, 'add_comment.html', context)


def handle_uploaded_file(f):
    with open('media_files/com_files/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def add_comment(request):
    context = {}
    if request.POST:
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['files'])
    else:
        form = CommentForm()
    context['form'] = form
    return render(request, 'add_comment.html', context)
