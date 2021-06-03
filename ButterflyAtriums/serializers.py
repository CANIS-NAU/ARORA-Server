from rest_framework import serializers

from . import models


class UserSuperflySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

        model = models.UserSuperfly


