from django import forms
from .models import Task, Comment


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }
