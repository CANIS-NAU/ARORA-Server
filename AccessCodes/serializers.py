from rest_framework import serializers
from . import models

class AccessCodesSerializers( serializers.ModelSerializer ):
	class Meta:
		fields = '__all__'
		model = models.AccessCodes
