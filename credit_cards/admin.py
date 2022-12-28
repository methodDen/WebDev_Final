from django.contrib import admin
from django.contrib.admin import ModelAdmin

from credit_cards.models import CreditCard


# Register your models here.
@admin.register(CreditCard)
class CreditCardAdmin(ModelAdmin):
    list_display = (
        "id",
        "card_number",
    )
