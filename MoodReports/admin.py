from django.contrib import admin

from .models import MoodReport, MoodType

admin.site.register(MoodReport)
admin.site.register(MoodType)
