from django.contrib import admin

from .models import UserInteraction, UserInteractionType, SuperflySession

class SuperflySessionAdmin(admin.ModelAdmin):
    list_display = ["participant_1"]

admin.site.register(UserInteraction)
admin.site.register(UserInteractionType)
admin.site.register(SuperflySession, SuperflySessionAdmin)
