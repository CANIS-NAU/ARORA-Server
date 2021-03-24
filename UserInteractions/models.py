from django.db import models
from UserInfos.models import UserInfo
from Quests.models import QuestReport
from Notifications.models import Notification
from Butterflies.models import Superfly

class UserInteractionType(models.Model):
    user_interaction_type_id = models.AutoField(primary_key=True, db_column='UserInteractionTypeId')  # Primary Key
    user_interaction_description = models.TextField(db_column='UserInteractionTypeDescription')

    def __int__(self):
        return self.user_interaction_type_id


# Create your models here.
class UserInteraction(models.Model):
    user_interaction_id = models.AutoField(primary_key=True, db_column='UserInteractionId')  # Primary Key
    user_interaction_created_at = models.DateTimeField(auto_now=True, db_column='UserInteractionCreatedAt')

    # Foreign Key, UserInfo:UserId -> UserInteraction:InitiatorUserId
    initiator_user_id = models.ForeignKey(UserInfo, related_name='initiator', on_delete=models.CASCADE,
                                          db_column='InitiatorUserId')

    # Foreign Key, UserInfo:UserId -> UserInteraction:ReceiverUserId
    receiver_user_id = models.ForeignKey(UserInfo, related_name='receiver', on_delete=models.CASCADE,
                                         db_column='ReceiverUserId')

    user_interaction_type_id = models.ForeignKey(UserInteractionType, on_delete=models.CASCADE,
                                                 db_column='UserInteractionTypeId')
    user_interaction_content = models.TextField(db_column='UserInteractionContent')

    # Need a field for a QuestReportID to which this interaction corresponds
    #quest_report_id = models.ForeignKey(QuestReport, on_delete=models.CASCADE, 
    #                                             db_column='QuestReportId', blank=True, 
    #                                             null=True, unique=False, editable=True)

    # Need a field for a Notification to which this interaction corresponds
    notification_id = models.ForeignKey(Notification, on_delete=models.CASCADE, 
                                                 db_column='NotificationId', blank=True, 
                                                 null=True, unique=False, editable=True)

    # Need a field for a QuestReportID to which this interaction corresponds
    #notification_id = models.ForeignKey(, on_delete=models.CASCADE, db_column='QuestReportId', default=1, unique=False, editable=True)
    def __str__(self):
        return self.user_interaction_content

#

#Model that houses the participants, progress, and superfly recipe for a superfly session.
class SuperflySession(models.Model):
    participant_1 = models.ForeignKey(UserInfo, related_name="participant1", 
            db_column="Participant1", null=True, blank=True, on_delete=models.CASCADE)
    participant_2 = models.ForeignKey(UserInfo, related_name="participant2", 
            db_column="Participant2", null=True, blank=True, on_delete=models.CASCADE)
    participant_3 = models.ForeignKey(UserInfo, related_name="participant3", 
            db_column="Participant3",null=True, blank=True, on_delete=models.CASCADE)
    participant_4 = models.ForeignKey(UserInfo, related_name="participant4", 
            db_column="Participant4", null = True, blank=True, on_delete=models.CASCADE)
    participant_5 = models.ForeignKey(UserInfo, related_name="participant5", 
            db_column="Participant5", null = True, blank=True, on_delete=models.CASCADE)
    superfly_recipe = models.ForeignKey(Superfly, on_delete=models.CASCADE)
    #Current amount of butterflies contributed in this session.
    current_b0_count = models.IntegerField(default=0, db_column="CurrentB0Count")
    current_b1_count = models.IntegerField(default=0, db_column="CurrentB1Count")
    current_b2_count = models.IntegerField(default=0, db_column="CurrentB2Count")
    current_b3_count = models.IntegerField(default=0, db_column="CurrentB3Count")
    current_b4_count = models.IntegerField(default=0, db_column="CurrentB4Count")

    """def completedSuperfly(self):
        b0 = self.superfly_recipe.b0_couwent
        return True"""

#Invite object that the user can accept or decline to join a session.
class SuperflyInvite(models.Model):
    session = models.ForeignKey(SuperflySession, db_column="Session", on_delete=models.CASCADE)
    recipiant = models.ForeignKey(UserInfo, db_column="Recipiant", on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)


    