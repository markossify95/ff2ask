from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .JSONserializer import *


# GETs the list of AudienceQuestions, POSTs new question
class AudienceQuestionList(APIView):
    def get(self, request):
        questions = AudienceQuestion.objects.all()
        serializer = AudienceQuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AudienceQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Audience votes for questions they like the most
# Teacher gets the sorted list of questions
# Voter class increments the value of score of particular question
class Voter(APIView):
    def get_object(self, pk):
        try:
            return AudienceQuestion.objects.get(pk=pk)
        except AudienceQuestion.DoesNotExist:
            raise Http404

    def put(self, request, pk):
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
