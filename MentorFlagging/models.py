from django.db import models
from django.utils.timezone import utc
from datetime import datetime

# Create your models here.
class Flagging( models.Model ):
	mentee_id = models.IntegerField( default=0, db_column="menteeId")
	mentor_id = models.IntegerField( default=0, db_column="mentorId")
	timestamp_flagged = models.DateTimeField(default=datetime(1979, 12, 31, 0, 0,  0, 000000, tzinfo=utc), db_column="timeFlagged")
	timestamp_resolved = models.DateTimeField(default=datetime(1979, 12, 31, 0, 0,  0, 000000, tzinfo=utc), db_column='timeResolved')
	reason_flagged = models.TextField( default="No reason logged", db_column="whyFlagged")
	how_resolved = models.TextField( default="Flag not resolved", db_column="howResolved")
