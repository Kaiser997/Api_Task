from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from api_task.models import Task
from api_task.models import Person
from api_task.serializer import TaskSerializer

def get_model_fields(model):
    return [field.name for field in model._meta.get_fields()]

class TaskListAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    #queryset = Task.objects.filter(name = "Crear endpoint" ).values("task_status")
    #queryset = Task.objects.order_by("name")
    #queryset = Task.objects.all().order_by("description").values()
    #queryset = Task.objects.all().order_by("-name").values()
    
    #queryset = Task.objects.all()[:2] #obtener una cantidad de objetos

    #queryset = Task.objects.count()

    #person = Person.objects.get(document = 3543513)
    #queryset = Task.objects.filter(person = person)

    #task= Task.objects.get(name = "modulo inicio de sesion")
    #queryset = Person.objects.filter

    #queryset = Task.objects.select_related("person").filter(person__name="brayan")
    #queryset = Task.objects.filter(person__name="roger")

      
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    filterset_fields = ('task_status', 'priority','person__document','delivery_date' )
    search_fields = get_model_fields(Task)

class TaskUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


