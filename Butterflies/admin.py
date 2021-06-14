from django.contrib import admin

# Register your models here.
from .models import Butterfly, UserButterfly, ButterflyComment, ButterflyLike, ButterflyType, Superfly

#Have the superflies displayed by their unique name.
class SuperflyAdmin(admin.ModelAdmin):
    list_display = ['superfly_name']

admin.site.register(Butterfly)
admin.site.register(UserButterfly)
admin.site.register(ButterflyType)
admin.site.register(ButterflyComment)
admin.site.register(ButterflyLike)
#Register a better view of the superfly on the admin site.
admin.site.register(Superfly,SuperflyAdmin)
