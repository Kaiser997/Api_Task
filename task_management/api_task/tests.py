from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from api_task.models import Person
from api_task.models import Task
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class PersonaTests(APITestCase):

    def setUp(self):
        self.person = Person.objects.create(
            name="brayan",
            last_name="rojas",
            document="155463129",
            document_type="CC",
            email="brayan@gmail.com",
            phone="33646840619",
        )

        self.user = User.objects.create_user(
            username="roger",
            email="kaiser@gmail.com",
            password="1997",
        )

        token = Token.objects.create(user=self.user)
        self.token = token.key
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)

    def test_create_person(self):
        url = reverse("personcreatelist")
        data = {
            "name": "roger",
            "last_name": "rubio",
            "document": "1013673129",
            "document_type": "CC",
            "email": "roger@gmail.com",
            "phone": "3007750619",
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.filter(document="1013673129").count(), 1)

    def test_update_person(self):
        url = reverse("personupdatedestroy", kwargs={"pk": self.person.pk})
        data = {"name": "johan"}

        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.get().name, "johan")

    def test_delete_persona(self):
        url = reverse("personupdatedestroy", kwargs={"pk": self.person.pk})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_task(self):
        url = reverse("taskcreatelist")
        data = {
            "name": "Crear endpoint",
            "description": "Debe realizar un endpoint para consultar personas",
            "task_status": "TODO",
            "priority": "ALTA",
            "delivery_date": "25 DE JULIO",
            "commentary": "Realizar la lectura de la documentacion Django rest framework",
            "person_id": self.person.pk
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.filter(priority="ALTA").count(), 1)
