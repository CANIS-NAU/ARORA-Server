
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import UserInfo


# Create UserInfoAdmin for UserInfo model.
class UserInfoAdmin(admin.ModelAdmin):
	#  Set attributes to be displayed
        list_display = ['username','user_id','user_points'] 
	# For more information, https://docs.djangoproject.com/en/2.2/ref/contrib/admin/

# let our admin-site know the new member coming
# Two arguments here, one is the model, the other is related admin class
admin.site.register(UserInfo, UserInfoAdmin)

