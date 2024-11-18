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
SEX =[
    ('m', 'Man'),
    ('w', 'Woman'),
]


class CreatedUpdatedAt(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    locale = models.CharField(max_length=50, null=True)
    sex = models.CharField(choices=SEX, max_length=2, null=True)

    def __str__(self):
        return self.last_name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(CreatedUpdatedAt):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Task(CreatedUpdatedAt):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, null=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=2, null=True)
    height_level = models.PositiveIntegerField(null=True)
    tags = models.ManyToManyField(Tag)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.title


class Comment(CreatedUpdatedAt):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    photo = models.ImageField(upload_to='com_photo', null=True)
    files = models.FileField(upload_to='com_files', null=True)

    def __str__(self):
        return f'{self.user.last_name} - {self.task.title}'


class Attachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file
