from rest_framework import serializers
from . import models

class MessageSerializers( serializers.ModelSerializer ):
	class Meta:
		fields = '__all__'
		model = models.Message
