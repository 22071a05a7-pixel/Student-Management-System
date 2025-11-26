# from django.test import TestCase
# from django.urls import reverse
# from rest_framework.test import APIClient
# from .models import Student

# # Create your tests here.

# class StudentAPITests(TestCase):

#     def setUp(self):
#         self.client = APIClient()
#         Student.objects.create(name="Test", email="test@demo.com", course="CS")

#     def test_list_students(self):
#         response = self.client.get("/api/students/")
#         self.assertEqual(response.status_code, 200)

#     def test_create_student(self):
#         data = {"name": "Unit Test", "email": "unit@example.com", "course": "ECE"}
#         response = self.client.post("/api/students/create/", data)
#         self.assertEqual(response.status_code, 200)

# class StudentTests(TestCase):
#     def test_create_student(self):
#         student = Student.objects.create(
#             name="Test Student",
#             email="test@example.com",
#             course="CS"
#         )
#         self.assertEqual(student.name, "Test Student")
    
#     def test_student_list_api(self):
#         response = self.client.get('/api/students/')
#         self.assertEqual(response.status_code, 200)

# from django.test import TestCase
# from django.urls import reverse
# from .models import Student

# class StudentModelTests(TestCase):
    
#     def test_create_student(self):
#         """Test creating a student object"""
#         student = Student.objects.create(
#             name="Test Student",
#             email="test@example.com",
#             course="Computer Science"
#         )
#         self.assertEqual(student.name, "Test Student")
#         self.assertEqual(student.email, "test@example.com")
        
#     def test_student_string_representation(self):
#         """Test student string representation"""
#         student = Student(name="John Doe")
#         self.assertEqual(str(student), "John Doe")

# class StudentViewTests(TestCase):
    
#     def test_student_list_view(self):
#         """Test the student list API endpoint"""
#         response = self.client.get('/api/students/')
#         # Should return 200 even if no students
#         self.assertIn(response.status_code, [200, 404])
        
#     def test_student_model_fields(self):
#         """Test student model has correct fields"""
#         student = Student()
#         self.assertTrue(hasattr(student, 'name'))
#         self.assertTrue(hasattr(student, 'email'))
#         self.assertTrue(hasattr(student, 'course'))

from django.test import TestCase
from .models import Student
import sys

class StudentTests(TestCase):
    
    def setUp(self):
        print("Setting up test data...")
        self.student = Student.objects.create(
            name="Test Student",
            email="test@example.com",
            course="Computer Science"
        )
    
    def test_student_creation(self):
        """Test that student objects can be created"""
        print("Testing student creation...")
        self.assertEqual(self.student.name, "Test Student")
        self.assertEqual(self.student.email, "test@example.com")
        print("✅ Student creation test passed!")
    
    def test_student_list_api(self):
        """Test the student list API"""
        print("Testing API endpoint...")
        response = self.client.get('/api/students/')
        self.assertEqual(response.status_code, 200)
        print("✅ API test passed!")
    
    def test_student_str_representation(self):
        """Test string representation"""
        print("Testing string representation...")
        self.assertEqual(str(self.student), "Test Student")
        print("✅ String representation test passed!")