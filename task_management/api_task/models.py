from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=True)
    document = models.CharField(max_length=200, null=False)
    document_type = models.CharField(max_length=5, null=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

class Task(models.Model):

    TASK_STATUS_CHOICES = [
        ("BACKLOG", "BACKLOG"),
        ("TODO", "TODO"),
        ("DOING", "DOING"),
        ("TEST", "TEST"),
        ("DONE", "DONE"),
    ]

    PRIORITY_CHOICES=[
        ("ALTA", "ALTA"),
        ("MEDIA", "MEDIA"),
        ("BAJA","BAJA")
    ]

    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=200, null=False)
    task_status = models.CharField(max_length=200, choices=TASK_STATUS_CHOICES)
    priority = models.CharField(max_length=200, choices=PRIORITY_CHOICES)
    delivery_date = models.DateField(max_length=200, null=False)
    commentary = models.CharField(max_length=200, null=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
