from django.urls import path
from .views import (
    TeacherListCreateView,
    TeacherDetailView,
    StudentListCreateView,
    StudentDetailView,
)

urlpatterns = [
    # Teacher
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),

    # Student
    path('students/', StudentListCreateView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
]
