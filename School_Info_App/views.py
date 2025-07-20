from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher_info_MODEL, Student_info_MODEL
from .serializers import TeacherInfoSerializer, StudentInfoSerializer

# ---- TEACHER API ----

class TeacherListCreateView(APIView):
    def get(self, request):
        teachers = Teacher_info_MODEL.objects.all()
        serializer = TeacherInfoSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetailView(APIView):
    def get_object(self, pk):
        try:
            return Teacher_info_MODEL.objects.get(pk=pk)
        except Teacher_info_MODEL.DoesNotExist:
            return None

    def get(self, request, pk):
        teacher = self.get_object(pk)
        if not teacher:
            return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TeacherInfoSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, pk):
        teacher = self.get_object(pk)
        if not teacher:
            return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TeacherInfoSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        teacher = self.get_object(pk)
        if not teacher:
            return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)
        teacher.delete()
        return Response({"message": "Teacher deleted"}, status=status.HTTP_204_NO_CONTENT)


# ---- STUDENT API ----

class StudentListCreateView(APIView):
    def get(self, request):
        students = Student_info_MODEL.objects.all()
        serializer = StudentInfoSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    def get_object(self, pk):
        try:
            return Student_info_MODEL.objects.get(pk=pk)
        except Student_info_MODEL.DoesNotExist:
            return None

    def get(self, request, pk):
        student = self.get_object(pk)
        if not student:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentInfoSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        if not student:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentInfoSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        if not student:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        student.delete()
        return Response({"message": "Student deleted"}, status=status.HTTP_204_NO_CONTENT)
