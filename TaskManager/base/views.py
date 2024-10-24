from functools import lru_cache

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from .forms import TaskForm, CommentForm
from .models import Task, User, Comment


def home(request):
    return HttpResponse("Welcome to our task management site")


class TasksView(TemplateView):
    template_name = 'tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_tasks())
        return context

    def get_tasks(self):
        return {
            'all': Task.objects.all(),
            'h_priority': Task.objects.filter(priority='h'),
            'm_priority': Task.objects.filter(priority='m').exclude(status=''),
            'start_with': Task.objects.filter(title__startswith='Создать'),
        }


class UsersView(TemplateView):
    template_name = 'users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = self.get_users()
        return context

    def get_users(self):
        return [
            {"name": "John", "age": 25, "phone": "123-456-7890", 'photo': 'john.jpg'},
            {"name": "Alice", "age": 30, "phone": "987-654-3210", 'photo': 'static/john.jpg'},
            {"name": "Bob", "age": 28, "phone": "555-123-4567", 'photo': 'static/john.jpg'},
            {"name": "Eva", "age": 22, "phone": "666-888-9999", 'photo': 'static/john.jpg'}
        ]


# Homework 4
@cache_page(60 * 30)
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
    with open('media_files/com_files/' + f.name, 'wb+') as destination:
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


# Функция, которая рекурсивно считает сумму положительных чисел списка
@lru_cache(maxsize=None)
def sum_positive(lst):
    if len(lst) == 0:
        return 0
    else:
        num = lst[0]
        if num > 0:
            return num + sum_positive(lst[1:])
        else:
            return sum_positive(list[1:])
