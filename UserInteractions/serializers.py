from rest_framework import serializers

from . import models
#from .models import *



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
    class Meta:
        #FIXME: This and the import break with random errors.
        #def getRandomRecipe(self):
         #   print("Ree")
          #  return Superfly.objects.order_by("?").first()
        model = models.SuperflySession
        fields = "__all__"
        #model.superfly = getRandomRecipe(self)

class SuperflyInviteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.SuperflyInvite
