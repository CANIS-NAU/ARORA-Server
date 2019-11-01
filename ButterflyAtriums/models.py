from django.db import models
from UserInfos.models import UserInfo
from Quests.models import QuestReport

# Create your models here.


class ButterflyAtrium(models.Model):
    butterfly_atrium_id = models.AutoField(primary_key=True, db_column='ButterflyAtriumId')  # Primary Key
     # Foreign Key, UserInfo:UserId -> UserInteraction:InitiatorUserId
    butterfly_atrium_user_id = models.ForeignKey(UserInfo, related_name='butterfly_atrium_user_id', on_delete=models.CASCADE,
                                          db_column='ButterflyAtriumUserId') 
    color_one_count = models.IntegerField(db_column="ColorOneCount", default=0)
    color_two_count = models.IntegerField(db_column="ColorTwoCount", default=0)
    color_three_count = models.IntegerField(db_column="ColorThreeCount", default=0)
    color_four_count = models.IntegerField(db_column="ColorFourCount", default=0)

    def __int__(self):
        return self.butterfly_atrium_id


