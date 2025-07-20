from rest_framework import serializers
from .models import Teacher_info_MODEL, Student_info_MODEL

class TeacherInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher_info_MODEL
        fields = '__all__'

class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_info_MODEL
        fields = '__all__'
