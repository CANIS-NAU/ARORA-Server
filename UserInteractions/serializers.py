from rest_framework import serializers

from . import models
from .models import Superfly
from Butterflies.serializers import SuperflySerializer



class UserInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.UserInteraction


class UserInteractionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.UserInteractionType

class SuperflySessionSerializer(serializers.ModelSerializer):
    session_id = serializers.IntegerField(read_only=True)
    superfly_recipe = SuperflySerializer(read_only=True)
    class Meta:
        model = models.SuperflySession
        fields = "__all__"

class SuperflyInviteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.SuperflyInvite
