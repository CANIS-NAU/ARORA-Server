from django.db import models
from UserInfos.models import UserInfo
from Quests.models import QuestReport
from ButterflyAtriums.models import ButterflyAtrium
# Create your models here.


class ButterflyType(models.Model):
    butterfly_type_id = models.AutoField(primary_key=True, default=1, db_column='ButterflyTypeId')  # Primary Key
    butterfly_type_description = models.IntegerField(db_column='ButterflyTypeDescription')
    butterfly_type_image = models.TextField(db_column='ButterflyTypeImage')

    def __int__(self):
        return self.butterfly_type_id


class Butterfly(models.Model):
    butterfly_id = models.AutoField(primary_key=True, db_column='ButterflyId')  # Primary Key

    # Foreign Key, ButterflyType:ButterflyTypeId -> Butterfly:ButterflyTypeId
    butterfly_type_id = models.ForeignKey(ButterflyType, on_delete=models.CASCADE, db_column='ButterflyTypeId')

    butterfly_create_at = models.DateTimeField(auto_now_add=True, db_column='ButterflyCreatedAt')

    def __int__(self):
        return self.butterfly_id

class Superfly(models.Model):
    superfly_id = models.AutoField(primary_key=True, db_column='SuperflyId') # Primary Key

    # Foreign Key, ButterflyAtrium:ButterflyAtriumTypeId -> Superfly:ButterflyAtriumId
    butterfly_atrium_id = models.ForeignKey(ButterflyAtrium, on_delete=models.CASCADE, db_column="ButterflyAtriumId")

    # Foreign Key, ButterflyType:ButterflyTypeId -> Superfly:ButterflyTypeId
    butterfly_type_id = models.ForeignKey(ButterflyType, on_delete=models.CASCADE, db_column='ButterflyTypeId')

class UserButterfly(models.Model):
    user_butterfly_id = models.AutoField(primary_key=True, db_column='UserButterflyId')  # Primary Key

    # Foreign Key, Butterfly:ButterflyId -> UserButterfly:ButterflyId
    butterfly_id = models.ForeignKey(Butterfly, on_delete=models.CASCADE, db_column='ButterflyId')

    time_caught = models.DateTimeField(auto_now_add=True, db_column='TimeCaught')

    # Foreign Key, UserInfo:UserId -> UserButterfly:UserId
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='UserId')

    def __int__(self):
        return self.user_butterfly_id


class ButterflyLike(models.Model):
    butterfly_like_id = models.AutoField(primary_key=True, db_column='ButterflyLikeId')  # Primary Key

    # Foreign Key, Butterfly:ButterflyId -> ButterflyLike:ButterflyId
    # butterfly_id = models.ForeignKey(Butterfly, on_delete=models.CASCADE, db_column='ButterflyId')

    # Foreign Key, UserInfo:UserId -> ButterflyLike:UserId
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='UserId')

    # Foreign Key, QusetReport:QuestReportId -> ButterflyLike:QusetReportId
    quest_report_id = models.ForeignKey(QuestReport, on_delete=models.CASCADE, db_column='QuestReportId', null=True)
    

    like_created_at = models.DateTimeField(auto_now_add=True, db_column='LikeCreatedAt')

    def __int__(self):
        return self.butterfly_like_id


class ButterflyComment(models.Model):
    butterfly_comment_id = models.AutoField(primary_key=True, db_column='ButterflyCommentId')  # Primary Key

    # Foreign Key, Butterfly:ButterflyId -> ButterflyComment:ButterflyId
    butterfly_id = models.ForeignKey(Butterfly, on_delete=models.CASCADE, db_column='ButterflyId')

    # Foreign Key, UserInfo:UserId -> ButterflyComment:UserId
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='UserId')

    comment_created_at = models.DateTimeField(auto_now_add=True, db_column='CommentCreatedAt')
    comment_text = models.TextField(db_column='CommentText')

    def __int__(self):
        return self.butterfly_comment_id
