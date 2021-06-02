from rest_framework import serializers

from . import models
from .models import Superfly
from Butterflies.serializers import SuperflySerializer
from UserInfos.serializers import UserInfoSerializer, UserSerializer



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
    #Set this SuperflySerializer to have the whole representation sent, rather than its id. 
    #Necessary to serialize the model into a Superfly model in the SuperflySession model client-side. 
    superfly_recipe = SuperflySerializer(read_only=True)
    #Do the same for each user in the list of participants. 
    participant_0 = UserInfoSerializer(many=False, required=False)
    #Use these too? Probably TODO for joining and viewing users. 
    participant_1 = UserInfoSerializer(required=False)
    participant_2 = UserInfoSerializer(required=False)
    participant_3 = UserInfoSerializer(required=False)
    participant_4 = UserInfoSerializer(required=False)
    class Meta:
        model = models.SuperflySession
        fields = "__all__"

class SuperflyInviteSerializer(serializers.ModelSerializer):
    session = SuperflySessionSerializer(read_only=True)
    class Meta:
        fields = '__all__'
        model = models.SuperflyInvite

class TradeRequestSerializer(serializers.ModelSerializer):
    sender = UserInfoSerializer(required=False)
    recipient = UserInfoSerializer(required=False)
    class Meta:
        fields = '__all__'
        model = models.TradeRequest
