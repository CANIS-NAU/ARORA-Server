from django.contrib import admin

# Register your models here.
from .models import Quest, QuestReport, QuestStatus, QuestType

admin.site.register(Quest)

admin.site.register(QuestReport)

admin.site.register(QuestStatus)

admin.site.register(QuestType)
