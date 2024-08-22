from rest_framework import serializers

from .models import Tag, Task

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id', 'is_default', 'created_at', 'updated_at']


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'tag', 'priority', 'date', 'time', 'repeat', ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']