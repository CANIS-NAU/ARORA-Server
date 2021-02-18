from rest_framework import serializers

from . import models


class UserInfoSerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(source='username', max_length=50)

    class Meta:
        fields = (
            'user_info_id',
            'user_current_mood_updated',
            'user_created_at',
            'user_catching_date',
            'user_name',
            'user_name_of_strength',
            'user_current_mood',
            'user_id',
            'user_b0_count',
            'user_b1_count',
            'user_b2_count',
            'user_b3_count',
            'user_b4_count',
            'user_b5_count',
            'user_current_location_lat',
            'user_current_location_long',
            'user_current_location_updated',
            'user_current_butterfly',
            'user_pollen')
        model = models.UserInfo


# Serializer for basic information of user-info model
class UserSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='username', max_length=50)
    user_email = serializers.CharField(source='email', max_length=50)

    class Meta:
        fields = ('user_id',
                  'user_name',
                  'user_email')
        model = models.UserInfo
