from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class ProfileAdmin(admin.ModelAdmin):
    model = Profile


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline, ]


admin.site.unregister(User)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(User, UserAdmin)

