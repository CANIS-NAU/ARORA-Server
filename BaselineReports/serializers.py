from rest_framework import serializers
from . import models


class BaselineReportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.BaselineReport
