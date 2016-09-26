from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .JSONserializer import *
from django.shortcuts import render, redirect
from django.template import loader, Context


# GETs the list of AudienceQuestions
class AudienceQuestionList(APIView):
    def get(self, request):
        questions = AudienceQuestion.objects.all()
        serializer = AudienceQuestionSerializer(questions, many=True)
        context = {
            'questions': serializer.data
        }
        return render(request, 'audience/audience_questions.html', context)

# GETs the form and POSTs new question
class NewAudienceQuestion(APIView):
    def get(self, request):
        return render(request, 'audience/question_form.html', {})

    def post(self, request):
        serializer = AudienceQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            questions = AudienceQuestion.objects.all()
            serializer = AudienceQuestionSerializer(questions, many=True)
            context = {
                'questions': serializer.data
            }
            return render(request, 'audience/audience_questions.html', context)
            #   return Response(serializer.data, status=status.HTTP_201_CREATED) Ali bolje da vraca novu listu pitanja a mozda i ne
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# R-U-D for particular AudienceQuestion
class AQInstance(APIView):
    def get_object(self, pk):
        try:
            return AudienceQuestion.objects.get(pk=pk)
        except AudienceQuestion.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        question = self.get_object(pk)
        serializer = AudienceQuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk):
        question = self.get_object(pk)
        d = {
            'id': pk,
            'aq_text': request.data['aq_text'],  # IZ FRONTA SALJI PODATKE POD ISTIM NAZIVIMA ATRIBUTA
            'score': 0
        }
        serializer = AudienceQuestionSerializer(question, data=d)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Audience votes for questions they like the most
# Teacher gets the sorted list of questions
# Voter class increments the value of score of particular question
class Voter(APIView):
    def get(self, request):
        questions = AudienceQuestion.objects.all()
        serializer = AudienceQuestionSerializer(questions, many=True)
        context = {
            'questions': serializer.data
        }
        return render(request, 'audience/vote_form.html', context)

    def get_object(self, pk):
        try:
            return AudienceQuestion.objects.get(pk=pk)
        except AudienceQuestion.DoesNotExist:
            raise Http404

    def put(self, request, pk):  # PROVERI DA LI RADI SA None!!!
        vote = self.get_object(pk)
        d = {
            'id': pk,
            'aq_text': vote.aq_text,
            'score': vote.score + 1
        }
        serializer = AudienceQuestionSerializer(vote, data=d)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    def put(self, request, pk): #PROVERI DA LI RADI SA NONE!!!
        vote = self.get_object(pk)
        d = {
            'id': pk,
            'aq_text': vote.aq_text,
            'score': vote.score + 1
        }
        serializer = AudienceQuestionSerializer(vote, data=d)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """