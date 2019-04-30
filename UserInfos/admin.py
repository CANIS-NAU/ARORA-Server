
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserInfo

admin.site.register(UserInfo, UserAdmin)

