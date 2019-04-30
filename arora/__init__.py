"""
Foreign Key Relationships:


                    -------->MoodReport
                    |
          UserId    |
UserInfo-------------------->BaselineReport
                    |
                    |
                    -------->LocationReport
                    |
                    |
                    -------->SystemReport
                    |
                    |
                    -------->QuestionReport



                                        ButterflyId
                                      --------------->ButterflyComment<------|
                                      |                                      |
                ButterflyTypeId       |       ButterflyId                    | UserId
ButterflyType ------------------> Butterfly -------------> UserButterfly<----|-------- UserInfo
                                      |                                      |
                                      | ButterflyId                          |
                                      ---------------> ButterflyLike<--------|


              quest_status_id
QuestStatus----------------------> Quest
              quest_type_id    |
QuestType  --------------------



         UserId                 QuestId
UserInfo--------->QuestReport<----------Quest


         InitiatorUserId/UserId
UserInfo-------------------------->UserInteraction
        |                      |
        -----------------------|
        ReceiverUserId/UserId
"""

"""
Pre-access database
Mood_type - views
User_interaction -views
quest_type -views
"""
