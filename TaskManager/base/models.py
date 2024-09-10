from django.db import models


STATUS_CHOICES = [
    ('op', 'Open'),
    ('cl', 'Close'),
    ('pr', 'Process'),
]
PRIORITY_CHOICES = [
    ('h', 'High'),
    ('m', 'Medium'),
    ('l', 'Low'),
]


class Task(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, null=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=2, null=True)
    height_level = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Projects(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
