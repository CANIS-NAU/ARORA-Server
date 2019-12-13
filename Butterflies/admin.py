from django.contrib import admin

# Register your models here.
from .models import Butterfly, UserButterfly, ButterflyComment, ButterflyLike, ButterflyType, Superfly

admin.site.register(Butterfly)
admin.site.register(UserButterfly)
admin.site.register(ButterflyType)
admin.site.register(ButterflyComment)
admin.site.register(ButterflyLike)
admin.site.register(Superfly)
