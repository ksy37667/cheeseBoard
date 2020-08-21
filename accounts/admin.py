from django.contrib import admin
from .models import Profile, User
# Register your models here.

class ProfileAdmin(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"


class UserAdmin(admin.ModelAdmin):
    inlines = (ProfileAdmin,)


admin.site.register(User,UserAdmin)