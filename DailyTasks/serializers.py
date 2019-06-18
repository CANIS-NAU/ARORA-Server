from rest_framework import serializers
from . import models

class DailyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.DailyTask


