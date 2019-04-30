from django.test import TestCase
from .models import Quest

class QuestTest(TestCase):
    """ Test module for Quest model """

    def setUp(self):
        Quest.objects.create(
            QuestId=1, QuestTypeId=1, QuestStatus=2
        )

    def test_get_status(self):
        test_quest = Quest.objects.create(
            QuestId=2, QuestTypeId=3, QuestStatus=4
        )
        self.assertEqual(
            test_quest.get_status(), "Quest Status #4"
        )
