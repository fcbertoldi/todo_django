from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Task, toggle_archived
from .serializers import TaskSerializer


class ListTask(generics.ListCreateAPIView):
    """"
    API endpoint for listing tasks.
    """
    queryset = Task.objects.filter(archived=False).order_by('creation_time')
    serializer_class = TaskSerializer


class DetailTask(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating task state, and destroying task.
    """
    queryset = Task.objects.filter(archived=False).order_by('creation_time')
    serializer_class = TaskSerializer


@api_view(['GET'])
def archive_task(request, **kwargs):
    toggle_archived(kwargs['pk'], True)
    return Response()


class ListArchived(generics.ListAPIView):
    """
    API endpoint for archived tasks.
    """
    queryset = Task.objects.filter(archived=True).order_by('creation_time')
    serializer_class = TaskSerializer


class DetailArchived(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, unarchiving, and destroying archived tasks.
    """
    queryset = Task.objects.filter(archived=True).order_by('creation_time')
    serializer_class = TaskSerializer


@api_view(['GET'])
def unarchive_task(request, **kwargs):
    toggle_archived(kwargs['pk'], False)
    return Response()
