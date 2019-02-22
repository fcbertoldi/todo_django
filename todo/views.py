from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """"
    API endpoint for listing tasks.
    """
    queryset = Task.objects.filter(archived=False).order_by('-creation_time')
    serializer_class = TaskSerializer


class ArchivedViewSet(viewsets.ModelViewSet):
    """
    API endpoint for archived tasks.
    """
    queryset = Task.objects.filter(archived=True).order_by('-creation_time')
    serializer_class = TaskSerializer
