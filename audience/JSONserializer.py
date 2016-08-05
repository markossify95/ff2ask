from rest_framework import serializers
from .models import *


class AudienceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudienceQuestion
        fields = '__all__'
