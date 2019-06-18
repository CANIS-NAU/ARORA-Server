from django.db import models
from UserInfos.models import UserInfo


# Create your models here.
class DailyTask(models.Model):
    daily_task_id = models.AutoField(primary_key=True, db_column='DailyTaskId')  # Primary Key
    daily_task_day = models.DateField(auto_now=True, db_column='DailyTaskDay')

    # Foreign Key, UserInfo:UserId -> DailyTask:UserId
    daily_task_user_id = models.ForeignKey(UserInfo, related_name='daily_task_user_id', on_delete=models.CASCADE, db_column='UserId')
    # Likes
    daily_task_likes_required = models.IntegerField(default=3, db_column='DailyTaskLikesRequired')
    daily_task_likes_achieved = models.IntegerField(default=0, db_column='DailyTaskLikesAchieved')

    # Butterflies
    daily_task_butterflies_required = models.IntegerField(default=3, db_column='DailyTaskButterfliesRequired')
    daily_task_butterflies_achieved = models.IntegerField(default=0, db_column='DailyTaskButterfliesAchieved')

    # M1
    daily_task_m1_required = models.IntegerField(default=1, db_column='DailyTaskM1Required')
    daily_task_m1_achieved = models.IntegerField(default=0, db_column='DailyTaskM1Achieved')

    # M2
    daily_task_m2_required = models.IntegerField(default=1, db_column='DailyTaskM2Required')
    daily_task_m2_achieved = models.IntegerField(default=0, db_column='DailyTaskM2Achieved')

    # M3
    daily_task_m3_required = models.IntegerField(default=1, db_column='DailyTaskM3Required')
    daily_task_m3_achieved = models.IntegerField(default=0, db_column='DailyTaskM3Achieved')

    def __str__(self):
        return self.daily_task_id
