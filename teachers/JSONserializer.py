from rest_framework import serializers
from .models import *


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherQuestion
        fields = '__all__'


class TQAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TQAnswer
        fields = '__all__'
