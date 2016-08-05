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


# R-U-D for teacher //read, update, delete
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
        }  # PAZI STA SALJES IZ FRONTA OVAMO, MORA DA BUDE DOBRO STRUKTUIRANO!
        serializer = TeacherQuestionSerializer(data=d)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Complete R-U-D for question
class QuestionInstance(APIView):
    def get_object(self, pk):
        try:
            return TeacherQuestion.objects.get(pk=pk)
        except TeacherQuestion.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        question = self.get_object(pk)
        serializer = TeacherQuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk):
        question = self.get_object(pk)
        serializer = TeacherQuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# GETs all answers for particular question, POSTs new answer
class AnswerList(APIView):
    def get(self, request, fk):
        answers = TQAnswer.objects.filter(question_id=fk)
        serializer = TQAnswerSerializer(answers, many=True)
        return Response(serializer.data)

    def post(self, request, fk):
        d = {
            'question_id': fk,
            'tq_answer_text': request.data['tq_answer_text'],
            'score': request.data['score']
        }  # PAZI STA SALJES IZ FRONTA OVAMO, MORA DA BUDE DOBRO STRUKTUIRANO!
        serializer = TQAnswerSerializer(data=d)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# R-U-D for particular Answer
class AnswerInstance(APIView):
    def get_object(self, pk):
        try:
            return TQAnswer.objects.get(pk=pk)
        except TQAnswer.DoesNotExist:
            raise Http404

    def get(self, request, fk, pk):
        answer = self.get_object(pk)
        serializer = TQAnswerSerializer(answer)
        return Response(serializer.data)

    def put(self, request, pk, fk):
        answer = self.get_object(pk)
        d = {
            'id': pk,
            'question_id': fk,
            'tq_answer_text': request.data['tq_answer_text'],
            'score': request.data['score']
        }
        serializer = TQAnswerSerializer(answer, data=d)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, fk):
        answer = self.get_object(pk)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# increments particular answer by 1
# First implement basic version, which doesnt depend on type of question
# I will later implement the version which checks the type of question for quicker action
class Voter(APIView):
    def get_object(self, pk):
        try:
            return TQAnswer.objects.get(pk=pk)
        except TQAnswer.DoesNotExist:
            raise Http404

    def put(self, request, pk, fk):
        answer = self.get_object(pk)
        d = {
            'id': pk,
            'tq_answer_text': answer.tq_answer_text,
            'score': answer.score + 1,
            'question_id': fk  # maybe extract this from answer object and not req, THINK ABOUT IT!
        }
        serializer = TQAnswerSerializer(answer, data=d)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
