from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from api_task.models import Person
from api_task.serializer import PersonSerializer

class PersonCountAPIView(APIView):
    def get(self, request):
        persons = Person.objects.annotate(task_count=Count('task'))
        data = [{'name' : person.name, 'task_count' : person.task_count }for person in persons]
        return Response(data)
    
class PersonsNameAPIView(APIView):
    def get(self, request):
        persons = Person.objects.values_list('name')
        return Response(list(persons))