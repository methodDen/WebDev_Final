from django.contrib import admin
from django.contrib.admin import ModelAdmin

from jusan.credit_cards.models import CreditCard


# Register your models here.
@admin.register(CreditCard)
class ProfileAdmin(ModelAdmin):
    list_display = (
        "id",
        "card_number",
    )
