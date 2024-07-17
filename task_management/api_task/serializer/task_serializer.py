from rest_framework import serializers
from api_task.models import Task
from api_task.serializer import PersonSerializer


class TaskSerializer(serializers.ModelSerializer):
    person = PersonSerializer(required=False)
    person_id = serializers.IntegerField(required=False)

    class Meta:
        model = Task
        fields = ["name", "description", "task_status", 
                  "priority", "delivery_date", "commentary", "person", "person_id"]

