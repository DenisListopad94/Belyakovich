from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to our task management site")


def tasks(request):
    return HttpResponse("Here you will see all your tasks")
