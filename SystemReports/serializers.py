from rest_framework import serializers

from . import models


class SystemReportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.SystemReport
