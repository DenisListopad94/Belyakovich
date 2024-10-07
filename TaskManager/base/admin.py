from django.contrib import admin
from django.utils.html import format_html

from base.models import Task, Project, Comment, Tag, Attachment, User


class TagsInline(admin.TabularInline):
    model = Task.tags.through


class TasksInline(admin.TabularInline):
    model = Task


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('project', 'title', 'description', 'display_status',
                    'priority', 'height_level', 'display_tags', 'user')
    inlines = [TagsInline, CommentInline]
    exclude = ['tags']

    def display_status(self, obj):
        if obj.status == 'cl':
            return format_html('<s>{}</s>', obj.title)
        return obj.title

    def display_tags(self, obj):
        return ', '.join([tag.name for tag in obj.tags.all()])


@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    inlines = [TasksInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['comment', 'photo']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [TagsInline]


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
