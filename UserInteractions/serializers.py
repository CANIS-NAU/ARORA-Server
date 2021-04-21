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
    class Meta:
        #FIXME: This and the import break with random errors.
        #def getRandomRecipe(self):
         #   print("Ree")
          #  return Superfly.objects.order_by("?").first()
        fields = '__all__'
        model = models.SuperflySession
        #model.superfly = getRandomRecipe(self)

class SuperflyInviteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.SuperflyInvite
