from rest_framework import serializers
from . import models


class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Phrase
