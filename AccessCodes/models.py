from django.db import models
from django.utils.timezone import utc
from datetime import datetime

# Create your models here.
class AccessCodes( models.Model ):
	access_code = models.TextField( default="" , db_column='accessCode')
	creator_id = models.IntegerField( default=2147483648, db_column='creatorId')
	created_at = models.DateTimeField( default=datetime(1979, 12, 31, 0, 0, 0, 000000, tzinfo=utc),
						db_column='dateCreated')
	expired_at = models.DateTimeField( default=datetime(1979, 12, 31, 0, 0, 0, 000000, tzinfo=utc),
						db_column='expiredAt')
