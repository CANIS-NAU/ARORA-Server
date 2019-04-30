from django.db import models
from UserInfos.models import UserInfo


# Create your models here.
class SystemReport(models.Model):
    system_report_id = models.AutoField(primary_key=True, db_column='SystemReportId')  # PK

    # Foreign Key, UserInfo:UserId -> SystemReport:UserId
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='UserId')

    power_level = models.IntegerField(db_column='PowerLevel')
    request_latency = models.TextField(db_column='RequestLatency')
    system_report_created_at = models.DateTimeField(auto_now_add=True, db_column='SystemReportCreatedAt')

    def __int__(self):
        return self.system_report_id
