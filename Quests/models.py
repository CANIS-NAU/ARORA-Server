from django.db import models
from UserInfos.models import UserInfo


# Create your models here.

class QuestStatus(models.Model):
    quest_status_id = models.AutoField(primary_key=True, db_column='QuestStatusId')  # Primary Key
    quest_status_description = models.TextField(db_column='QuestStatusDescription')

    def __int__(self):
        return self.quest_status_id


class QuestType(models.Model):
    quest_type_id = models.AutoField(primary_key=True, db_column='QuestTypeId')  # Primary Key
    quest_type_description = models.TextField(db_column='QuestTypeDescription')

    def __int__(self):
        return self.quest_type_id


class Quest(models.Model):
    quest_id = models.AutoField(primary_key=True, db_column='QuestId')  # Primary Key
    quest_type_id = models.ForeignKey(QuestType, on_delete=models.CASCADE, db_column='QuestTypeId')
    quest_status_id = models.ForeignKey(QuestStatus, on_delete=models.CASCADE, db_column='QuestStatus')

    def __int__(self):
        return self.quest_id

    def get_status(self):
        return 'Quest Status #' + str(self.quest_status)


class QuestReport(models.Model):
    quest_report_id = models.AutoField(primary_key=True, db_column='QuestReportId')  # Primary Key

    # Foreign Key, QuestType:QuestTypeId -> QuestReport:QuestId
    quest_type_id = models.ForeignKey(QuestType, on_delete=models.CASCADE, db_column='QuestTypeId', default=1)

    # Foreign Key, QuestStatus:QuestStatusId -> QuestReport:QuestId
    quest_status_id = models.ForeignKey(QuestStatus, on_delete=models.CASCADE, db_column='QuestStatusId', default=1)


    # Foreign Key, UserInfo:UserId -> QuestReport:UserId
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='UserId')

    quest_started_at = models.DateTimeField(auto_now_add=True, db_column='QuestStartedAt')
    quest_ended_at = models.DateTimeField(auto_now=True, db_column='QuestCompletedAt')

    def __int__(self):
        return self.quest_report_id
