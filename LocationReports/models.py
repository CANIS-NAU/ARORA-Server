from django.db import models
from UserInfos.models import UserInfo


# Create your models here.
class LocationReport(models.Model):
    location_report_id = models.AutoField(primary_key=True, db_column='LocationReportId')  # Primary Key

    location_report_lat = models.DecimalField(max_digits=5, decimal_places=2, db_column='LocationReportLat')
    location_report_long = models.DecimalField(max_digits=5, decimal_places=2, db_column='LocationReportLong')
    location_report_create_at = models.DateTimeField(auto_now_add=True, db_column='LocationReportCreatedAt')

    # Foreign Key, UserInfo:UserId -> LocationReport:UserId
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='UserId')

    def __int__(self):
        return self.LocationReportId
