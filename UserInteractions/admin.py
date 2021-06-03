from django.contrib import admin

from .models import UserInteraction, UserInteractionType, SuperflySession, SuperflyInvite, TradeRequest

class SuperflySessionAdmin(admin.ModelAdmin):
    list_display = ["session_id"]

admin.site.register(UserInteraction)
admin.site.register(UserInteractionType)
admin.site.register(SuperflySession, SuperflySessionAdmin)
admin.site.register(SuperflyInvite)
admin.site.register(TradeRequest)
