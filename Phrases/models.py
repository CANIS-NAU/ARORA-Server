from django.db import models


# Create your models here.
class Phrase(models.Model):
    phrase_id = models.AutoField(primary_key=True, db_column='PhraseId')  # Primary Key
    phrase_english_text = models.TextField(db_column='PhraseEnglishTexts')
    phrase_indigenous_text = models.TextField('PhraseIndigenousText')

    def __int__(self):
        return self.phrase_id
