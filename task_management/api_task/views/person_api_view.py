from rest_framework import generics
from rest_framework_datatables.pagination import DatatablesPageNumberPagination
from api_task.models import Person
from api_task.serializer import PersonSerializer
import django_filters.rest_framework
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count

class PersonListAPIView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    queryset = Person.objects.annotate(task_count=Count('task'))
    serializer_class = PersonSerializer
    pagination_class = DatatablesPageNumberPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_fields = ['name']
    ordering_fields = ['name'] #ordenar en el paginado por apellidos
    search_fields = ['name', 'last_name', 'document']
    
class PersonUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer