from django.db import models
from UserInfos.models import UserInfo
from Butterflies.models import Superfly

# Create your models here.

#This model represents a superfly that the user created.
#In essence, it ties the user to a superfly recipe, which is the superfly they made. 
class UserSuperfly(models.Model):
    user_superfly_id = models.AutoField(primary_key=True, db_column="UserSuperflyId")
    id_user = models.IntegerField(default=-1, db_column="UserId")
    id_superfly = models.IntegerField(default=-1, db_column="SuperflyId")
    user = models.ForeignKey(UserInfo, null=True, blank=True, on_delete=models.CASCADE, db_column="UserObj")
    superfly = models.ForeignKey(Superfly, null=True, blank=True, on_delete=models.CASCADE, db_column="SuperflyObj")
     


    def __int__(self):
        return self.user_superfly_id


