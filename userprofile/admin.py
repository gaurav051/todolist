from django.contrib import admin
from userprofile.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
                "user",
                "first_name",
                "middle_name",
                "last_name",
                "contact",
            )