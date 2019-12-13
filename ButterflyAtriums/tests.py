from django.test import TestCase
from .models import ButterflyType, Butterfly, UserButterfly, ButterflyLike, ButterflyComment


# Create your tests here.

class ButterflyTest(TestCase):
    """ Test module for Butterfly models """

    def setUp(self):
        testButterflytype = ButterflyType.objects.create(
            ButterflyTypeDescription="Butterfly description...",
            ButterflyTypeImage="Butterfly type image..."
        )
        Butterfly.objects.create(
            ButterflyTypeId=testButterflytype
        )

    def test_foriegn_key(self):
        testButterflytype = ButterflyType.objects.create(
            ButterflyTypeDescription="Butterfly description...",
            ButterflyTypeImage="Butterfly type image..."
        )
        testButterfly = Butterfly.objects.create(
            ButterflyTypeId=testButterflytype
        )
        self.assertEqual(
            testButterfly.ButterflyTypeId, testButterflytype
        )
