from rest_framework import serializers

from . import models


class MoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.MoodType


class MoodReportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.MoodReport
