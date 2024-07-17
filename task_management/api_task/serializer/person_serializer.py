from rest_framework import serializers
from api_task.models import Person


class PersonSerializer(serializers.ModelSerializer):
    task_count = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ["name", "last_name", "document", 
                  "document_type", "email", "phone", "task_count"]
        
    def get_task_count(self, obj):
        return obj.task_count if hasattr(obj, 'task_count') else 0
