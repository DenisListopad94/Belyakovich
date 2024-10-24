from django import forms
from base.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'status', 'priority', 'height_level', 'tags', 'user']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
