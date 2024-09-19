from django.contrib import admin
from base.models import Task, Project, Comment, Tag, Attachment, User


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
