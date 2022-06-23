from django.db import models
from django.utils.timezone import utc
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    user_info_id = models.AutoField(primary_key=True, db_column='UserInfoId')  # PK
    #Date since most recent mood report POST.
    user_current_mood_updated = models.DateTimeField(default=datetime(1979, 12, 31, 0, 0, 0, 000000, tzinfo=utc),
                                                       db_column='UserCurrentMoodUpdated')
    #user_created_at = models.DateTimeField(auto_now_add=True, editable=False, db_column='UserCreatedAt')
    #user_catching_date = models.DateTimeField(default=datetime(1979, 12, 31, 0, 0, 0, 000000, tzinfo=utc), db_column='UserCatchingDate')    
    user_current_stress = models.IntegerField(default=0, db_column='UserCurrentStress')
    user_current_mood = models.IntegerField(default=0, db_column='UserCurrentMood')
    user_id = models.IntegerField(default=2147483648, unique=False, editable=False, db_column='UserId')
    user_type = models.TextField(default='youth' , db_column='userType')
    mentor_id = models.IntegerField( default=2147483648 , db_column="MentorId")
    #Butterfly Counts, an inventory of butterflies caught in M4 for the current user. Composite attribute 
    #These counts are used to display in the atrium and create superflies in the superfly multiplayer game. 
    user_b0_count = models.IntegerField(default=0, db_column="UserB0Count") # Red
    user_b1_count = models.IntegerField(default=0, db_column="UserB1Count") # Yellow   
    user_b2_count = models.IntegerField(default=0, db_column="UserB2Count") # Orange   
    user_b3_count = models.IntegerField(default=0, db_column="UserB3Count") # Green    
    user_b4_count = models.IntegerField(default=0, db_column="UserB4Count") # Blue   
    
    #user_current_location_lat = models.DecimalField(max_digits=5, decimal_places=2, default=0.0,
     #                                               db_column='UserCurrentLocationLat')
    #user_current_location_long = models.DecimalField(max_digits=5, decimal_places=2, default=0.0,
    #                                                 db_column='UserCurrentLocationLong')
    #user_current_location_updated = models.DateTimeField(default=datetime(1979, 12, 31, 0, 0, 0, 000000, tzinfo=utc),
    #                                                     db_column='UserCurrentLocationUpdated')
    # This is the butterfly that displays on the profile page, not currently editable from the mobile app. 
    user_current_butterfly = models.IntegerField(default=0, db_column='UserCurrentButterfly')
    # This is the pollen gained from doing the mindfulness activities. It is spent to enter the butterfly catching game. 
    user_pollen = models.IntegerField(default=0, db_column='UserPollen')

    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['email']#, 'user_name']

    def __str__(self):
        return self.username
