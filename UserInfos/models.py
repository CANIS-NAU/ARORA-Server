from django.db import models
from django.utils.timezone import utc
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    user_info_id = models.AutoField(primary_key=True, db_column='UserInfoId')  # PK

    user_current_mood_updated = models.DateTimeField(default=datetime(1979, 12, 31, 0, 0, 0, 000000, tzinfo=utc),
                                                     db_column='UserCurrentMoodUpdated')
    user_created_at = models.DateTimeField(auto_now_add=True, editable=False, db_column='UserCreatedAt')
    user_name_of_strength = models.TextField(default='', db_column='UserNameOfStrength')
    user_current_mood = models.IntegerField(default=0, db_column='UserCurrentMood')
    user_id = models.IntegerField(default=2147483648, unique=False, editable=False, db_column='UserId')
    user_current_location_lat = models.DecimalField(max_digits=5, decimal_places=2, default=0.0,
                                                    db_column='UserCurrentLocationLat')
    user_current_location_long = models.DecimalField(max_digits=5, decimal_places=2, default=0.0,
                                                     db_column='UserCurrentLocationLong')
    user_current_location_updated = models.DateTimeField(default=datetime(1979, 12, 31, 0, 0, 0, 000000, tzinfo=utc),
                                                         db_column='UserCurrentLocationUpdated')
    user_current_butterfly = models.IntegerField(default=0, db_column='UserCurrentButterfly')
    user_pollen = models.IntegerField(default=0, db_column='UserPollen')
    user_points = models.IntegerField(default=0, db_column='UserPoints')

    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
