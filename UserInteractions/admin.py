from django.contrib import admin

from .models import UserInteraction, UserInteractionType

admin.site.register(UserInteraction)
admin.site.register(UserInteractionType)
