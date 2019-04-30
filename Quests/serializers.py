from rest_framework import serializers

from . import models


class QuestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.QuestType


class QuestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.QuestStatus


class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Quest


class QuestReportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.QuestReport
