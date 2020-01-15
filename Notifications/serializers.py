from rest_framework import serializers

from . import models

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Notification

class NotificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.NotificationType
