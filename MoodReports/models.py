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

    mood_type = models.IntegerField(db_column='MoodType')  # Not use foreign key here. For all reports in database
    user_text = models.TextField(db_column='UserText')

    def __str__(self):
        return self.user_text

    def __int__(self):
        return self.mood_report_id
