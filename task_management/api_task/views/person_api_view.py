from rest_framework import generics
from api_task.models import Person
from api_task.serializer import PersonSerializer

class PersonListAPIView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer