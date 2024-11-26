from collections import deque
from django.db import models


class Queue(models.Model):
    element = models.CharField(max_length=255, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)  # время добавления элемента в очередь

    def __str__(self):
        return self.element

    class Meta:
        ordering = ['timestamp']  # по fifo время добавления


class UniqueQueue:
    def add(self, element):
        if not Queue.objects.filter(element=element).exists():
            Queue.objects.create(element=element)

    def pop(self):
        try:
            element = Queue.objects.first()
            if element:
                element.delete()
                return element.element
        except Queue.DoesNotExist:
            return None

    def peek(self):
        element = Queue.objects.first()
        if element:
            return element.element
        return None

    def get_length(self):
        return Queue.objects.count()

    def get_last_element(self):
        element = Queue.objects.last()
        if element:
            return element.element
        return None

    def is_empty(self):
        return Queue.objects.count() == 0

    # Возвращаем все элементы в порядке добавления
    def __str__(self):
        return ', '.join([str(item.element) for item in Queue.objects.all()])
