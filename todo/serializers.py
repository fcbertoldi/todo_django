from .models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    state = serializers.CharField(source='get_state_display')

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'state')
