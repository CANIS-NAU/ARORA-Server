from django.db import models
from UserInfos.models import UserInfo


# Create your models here.

class MoodType(models.Model):
    mood_type_id = models.AutoField(primary_key=True, db_column='MoodTypeId')  # Primary Key
    mood_type_description = models.TextField(db_column='MoodTypeDescription')

    def __str__(self):
        return self.mood_type_description


class MoodReport(models.Model):
    mood_report_id = models.AutoField(primary_key=True, db_column='MoodReportId')  # Primary Key
    mood_report_created_at = models.DateTimeField(auto_now_add=True, db_column='MoodReportCreatedAt')

    # Foreign Key, UserInfo:UserId -> MoodReport:UserId
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='UserId')

    # Q1
    q1_response = models.IntegerField(db_column="Q1MoodResponse", default=1)

    # Q2
    q2_response = models.IntegerField(db_column="Q2MoodResponse", default=1)

    def __int__(self):
        return self.mood_report_id
