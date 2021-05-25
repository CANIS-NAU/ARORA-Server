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
    session_id = models.AutoField(primary_key=True, db_column="SessionId")
    session_start_date = models.DateTimeField(auto_now = True, db_column="SessionStartDate")
    session_participant_count = models.IntegerField(default=1, db_column="ParticipantCount") # How many users are in the session
    session_started = models.BooleanField(default=False) #Has the game started with enough participants?
    #user_ids for each participant in the session
    id_0 = models.IntegerField(default=-1, db_column = "P0Id")
    id_1 = models.IntegerField(default=-1, db_column = "P1Id")
    id_2 = models.IntegerField(default=-1, db_column = "P2Id")
    id_3 = models.IntegerField(default=-1, db_column = "P3Id")
    id_4 = models.IntegerField(default=-1, db_column = "P4Id")
    #Actual foreign key objects for each participant, corresponding with the 5 ids above.  
    participant_0 = models.ForeignKey(UserInfo, db_column="Participant0", related_name="participant_0", null=True, blank = True, on_delete=models.CASCADE)
    participant_1 = models.ForeignKey(UserInfo, db_column="Participant1", related_name="participant_1", null=True, blank=True, on_delete=models.CASCADE)
    participant_2 = models.ForeignKey(UserInfo, db_column="Participant2", related_name="participant_2", null=True, blank=True, on_delete=models.CASCADE)
    participant_3 = models.ForeignKey(UserInfo, db_column="Participant3", related_name="participant_3", null=True, blank=True, on_delete=models.CASCADE)
    participant_4 = models.ForeignKey(UserInfo, db_column="Participant4", related_name="participant_4", null=True, blank=True, on_delete=models.CASCADE)
    superfly_recipe = models.ForeignKey(Superfly, default = 1, blank=True, on_delete=models.CASCADE)
    #CurrentCounts: Current amount of butterflies contributed in this session.
    current_b0_count = models.IntegerField(default=0, db_column="CurrentB0Count")
    current_b1_count = models.IntegerField(default=0, db_column="CurrentB1Count")
    current_b2_count = models.IntegerField(default=0, db_column="CurrentB2Count")
    current_b3_count = models.IntegerField(default=0, db_column="CurrentB3Count")
    current_b4_count = models.IntegerField(default=0, db_column="CurrentB4Count")

    #Checks to see if the counts of b0-b4 are sufficient to create the superfly.
    def completedSuperfly(self):
        return (current_b0_count >= superfly_recipe.b0_count_needed 
        and current_b1_count >= superfly_recipe.b1_count_needed 
        and current_b2_count >= superfly_recipe.b2_count_needed 
        and current_b3_count >= superfly_recipe.b3_count_needed 
        and current_b4_count >= superfly_recipe.b4_count_needed)

#Invite object that the user can accept or decline to join a session.
class SuperflyInvite(models.Model):
    invite_id = models.AutoField(primary_key=True, db_column="InviteId")
    session = models.ForeignKey(SuperflySession, db_column="Session", on_delete=models.CASCADE)
    recipient = models.ForeignKey(UserInfo, db_column="Recipient", on_delete=models.CASCADE)
    uid_recipient = models.IntegerField(default = -1, db_column="RecipientId")
    accepted = models.BooleanField(default=False)


    