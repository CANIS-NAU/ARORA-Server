from django.db import models

# Create your models here.
class AccessCodes( models.Model ):
	access_code = models.TextField( default="" , db_column='accessCode')
