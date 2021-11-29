from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from graphics_base.models import Profile


class ProfileInlineAdmin(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "user profile"
    fieldsets = (
        (None, {"fields": ("user", "preferred_byline")}),
        ("Google", {"fields": ("google_email",)}),
        ("Twitter", {"fields": ("twitter_handle",)}),
    )


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInlineAdmin,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
