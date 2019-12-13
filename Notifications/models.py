from django.db import models
from UserInfos.models import UserInfo

# Create your models here.
class NotificationType(models.Model):
    notification_type_id = models.AutoField(primary_key=True, db_column='NotificationTypeId')  # Primary Key
    notification_type_description = models.TextField(db_column='NotificationTypeDescription')

    def __int__(self):
        return self.notification_type_id


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True, db_column='NotificationId')  # Primary Key

    notification_type_id = models.ForeignKey(NotificationType, on_delete=models.CASCADE, db_column='NotificationTypeId')

    notification_created_at = models.DateTimeField(auto_now_add=True, db_column='NotificationCreatedAt')

    # Foreign Key
    notification_user_id = models.ForeignKey(UserInfo, related_name='notification_user', on_delete=models.CASCADE,
                                          db_column='NotificationUserId') 

    def __int__(self):
        return self.notification_id

