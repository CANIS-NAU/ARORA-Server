from django.db import models
from django.utils.timezone import utc
from datetime import datetime
# Create your models here.

class Message():
	message_id = models.AutoField(primary_key=True, db_column='messageId')


	message_text = models.TextField(default="", db_column='messageText')
	message_date = models.DateTimeField(default=datetime(1979, 12, 31, 0, 0,  0, 000000, tzinfo=utc,
											db_column='messageTime')
	message_sender_id = models.IntegerField(default=2, db_column='senderId')
	sender_name = models.IntegerField(default='default-sender', db_column='senderName')

	def __init__( self ):
	  return self.messageId
