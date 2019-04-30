from rest_framework import serializers

from . import models


class LocationReportSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.LocationReport
