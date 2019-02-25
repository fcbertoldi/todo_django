from rest_framework import viewsets
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer


class ListTask(generics.ListCreateAPIView):
    """"
    API endpoint for listing tasks.
    """
    queryset = Task.objects.filter(archived=False).order_by('creation_time')
    serializer_class = TaskSerializer


class ListArchived(generics.ListAPIView):
    """
    API endpoint for archived tasks.
    """
    queryset = Task.objects.filter(archived=True).order_by('creation_time')
    serializer_class = TaskSerializer
