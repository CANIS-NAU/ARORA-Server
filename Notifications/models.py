from django.db import models
from UserInfos.models import UserInfo
from DailyTasks.models import DailyTask
from Quests.models import QuestReport

# Create your models here.
class NotificationType(models.Model):
    notification_type_id = models.AutoField(primary_key=True, db_column='NotificationTypeId')  # Primary Key
    notification_type_description = models.TextField(db_column='NotificationTypeDescription')

    def __int__(self):
        return self.notification_type_id

class CommentType(models.Model):
    comment_type_id = models.AutoField(primary_key = True, db_column='CommentTypeId') # Primary Key
    comment_type_description = models.TextField(db_column='CommentTypeDescription')
    
    def __int__(self):
        return self.comment_type_id

#Remnants of old early invite system, scrapped for now. 
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True, db_column='NotificationId')  # Primary Key

    notification_type_id = models.ForeignKey(NotificationType, on_delete=models.CASCADE, db_column='NotificationTypeId')

    notification_created_at = models.DateTimeField(auto_now_add=True, db_column='NotificationCreatedAt')

    #Foreign Keys
    #The following will be filled depending on the correspoding notification type:
    #Self???????
    like_pointer_id = models.ForeignKey("self", related_name='notif_like_ptr', on_delete=models.CASCADE,
                                           null=True, blank= True)

    comment_pointer_id = models.ForeignKey(CommentType, related_name='notif_commt_ptr', on_delete=models.CASCADE,
                                           null=True, db_column='CommentTypeId')

    quest_report_pointer_id = models.ForeignKey(QuestReport, related_name='notif_quest_ptr', on_delete=models.CASCADE,
                                           null=True, blank= True, db_column='QuestReportId')
    
    #TO DO: Need to create a game lobby before this is implemented
    #invitation_pointer_id = models.ForeignKey(UserInfo, related_name='notif_inv_ptr', on_delete=models.CASCADE,
    #                                      , null=True, blank= True, db_column='NotificationUserId')
    
    task_alert_pointer_id = models.ForeignKey(DailyTask, related_name='notif_task_ptr', on_delete=models.CASCADE,
                                           null=True, blank= True, db_column='DailyTaskId')


    def __int__(self):
        return self.notification_id

