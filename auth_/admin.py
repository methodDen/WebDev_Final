from django.contrib import admin
from django.contrib.admin import ModelAdmin

from auth_.models import MainUser, Profile

# Register your models here.


@admin.register(MainUser)
class MainUserAdmin(ModelAdmin):
    list_display = (
        "id",
        "email",
    )
    ordering = ("id",)


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = (
        "id",
        "user",
    )
