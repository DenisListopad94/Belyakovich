from django.contrib import admin
from base.models import Task, Projects


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    pass
