from rest_framework import serializers
from . import models

class FlaggingSerializer( serializers.ModelSerializer ):
	class Meta:
		fields = '__all__'
		model = models.Flagging
