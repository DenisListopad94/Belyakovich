import datetime
from base.models import Comment, SEX, User, Task, Project, STATUS_CHOICES, PRIORITY_CHOICES, Tag, Attachment

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'age', 'locale', 'sex']


class CommentSerializer(serializers.Serializer):
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    comment = serializers.CharField()
    photo = serializers.ImageField(allow_null=True)
    files = serializers.FileField(allow_null=True)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.task = validated_data.get('task', instance.task)
        instance.user = validated_data.get('user', instance.user)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.files = validated_data.get('files', instance.files)
        instance.save()
        return instance


class TaskSerializer(serializers.Serializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    title = serializers.CharField(max_length=64)
    description = serializers.CharField(max_length=256)
    status = serializers.ChoiceField(choices=STATUS_CHOICES, allow_null=True)
    priority = serializers.ChoiceField(choices=PRIORITY_CHOICES, allow_null=True)
    height_level = serializers.IntegerField(allow_null=True)
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.project = validated_data.get('project', instance.project)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.height_level = validated_data.get('height_level', instance.height_level)
        instance.tags.set(validated_data.get('tags', instance.tags.all()))
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance


class AttachmentSerializer(serializers.Serializer):
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())
    file = serializers.CharField(max_length=100)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        return Attachment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.task = validated_data.get('task', instance.task)
        instance.file = validated_data.get('file', instance.file)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance
