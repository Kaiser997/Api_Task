from rest_framework import serializers
from api_task.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["name", "last_name", "document", 
                  "document_type", "email", "phone"]
