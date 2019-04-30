from django.db import models
from UserInfos.models import UserInfo


# Create your models here.
class BaselineReport(models.Model):
    baseline_report_id = models.AutoField(primary_key=True, db_column='BaselineReportId')  # Primary Key

    # Foreign Key, UserInfo:UserId -> BaselineReport:UserId
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='UserId')

    baseline_report_created_at = models.DateTimeField(auto_now_add=True, db_column='BaselineReportCreatedAt')
    baseline_report_results = models.TextField(db_column='BaselineReportResults')  # Make longer

    def __int__(self):
        return self.baseline_report_id
