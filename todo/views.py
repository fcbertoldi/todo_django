from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view, action

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.filter(archived=False).order_by('creation_time')
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def archive(self, request, pk=None):
        task = self.get_object()
        task.toggle_archived()
        return Response()


class ArchivedTaskViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    queryset = Task.objects.filter(archived=True).order_by('creation_time')
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def unarchive(self, request, pk=None):
        task = self.get_object()
        task.toggle_archived()
        return Response()
