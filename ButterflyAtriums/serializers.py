from rest_framework import serializers
from Butterflies.serializers import SuperflySerializer
from UserInfos.serializers import UserInfoSerializer

from . import models


class UserSuperflySerializer(serializers.ModelSerializer):
    superfly = SuperflySerializer(read_only=True, required=False)
    user = UserInfoSerializer(read_only=True, required=False)
    class Meta:
        fields = '__all__'
        model = models.UserSuperfly


