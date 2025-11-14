from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Student

# Create your tests here.

class StudentAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        Student.objects.create(name="Test", email="test@demo.com", course="CS")

    def test_list_students(self):
        response = self.client.get("/api/students/")
        self.assertEqual(response.status_code, 200)

    def test_create_student(self):
        data = {"name": "Unit Test", "email": "unit@example.com", "course": "ECE"}
        response = self.client.post("/api/students/create/", data)
        self.assertEqual(response.status_code, 200)