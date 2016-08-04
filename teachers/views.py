from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .JSONserializer import *


# Lists all teachers and posts new instance
class TeacherList(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Complete CRUD for teacher
class TeacherInstance(APIView):
    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, pk):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        teacher = self.get_object(pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Lists all questions by single teacher, POSTs NEW QUESTION FOR TEACHER!
class QuestionList(APIView):
    def get(self, request, fk):
        questions = TeacherQuestion.objects.filter(teacher_id=fk)
        serializer = TeacherQuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, fk):
        d = {
            'teacher_id': fk,
            'tq_type': request.data['tq_type'],
            'tq_text': request.data['tq_text']  # OVAKO DOKTOR IZVLACI PODATKE
        }
        serializer = TeacherQuestionSerializer(data=d)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
