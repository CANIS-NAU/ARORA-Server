from rest_framework import serializers

from . import models


class ButterflyAtriumSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

        model = models.ButterflyAtrium


