from django.contrib import admin
from django.contrib.admin import ModelAdmin

from transactions.models import Transaction


# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(ModelAdmin):
    list_display = (
        "id",
        "source_card",
        "transaction_type",
    )


# Register your models here.
