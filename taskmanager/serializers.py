from rest_framework import serializers

from .models import Tag, Task

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id', 'is_default', 'created_at', 'updated_at']


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.EmailField(source='user.email', read_only=True)  # Get the email of the user
    tag = serializers.StringRelatedField() # This will call __str__ method of Tag class.

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'tag', 'priority', 'date', 'time', 'repeat', 'user' ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']