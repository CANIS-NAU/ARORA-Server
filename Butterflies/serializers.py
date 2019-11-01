from rest_framework import serializers

from . import models


class ButterflyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

        model = models.ButterflyType


class ButterflySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Butterfly


class SuperflySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Superfly


class UserButterflySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.UserButterfly


class ButterflyLikeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.ButterflyLike


class ButterflyCommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.ButterflyComment
