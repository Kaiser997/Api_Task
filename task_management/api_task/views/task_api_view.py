from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from api_task.models import Task
from api_task.serializer import TaskSerializer

class TaskListAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    filterset_fields = ('task_status', 'priority')
    search_fields = ['name']

class TaskUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


