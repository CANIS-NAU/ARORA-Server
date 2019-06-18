from django.contrib import admin

# Register your models here.
from .models import DailyTask

admin.site.register(DailyTask)
