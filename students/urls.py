from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_students),
    path('create/', views.create_student),
    path('<int:pk>/update/', views.update_student),
    path('<int:pk>/delete/', views.delete_student),
    path('page/', views.students_page, name='students_page'),
    path('page/<int:pk>/', views.student_detail, name='student_detail'),
]





