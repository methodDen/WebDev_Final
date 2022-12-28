from django.db import models

from credit_cards.models import CreditCard
from jusan import settings
from mixins.models import TimestampMixin

# Create your models here.


class Transaction(TimestampMixin):
    TRANSFER = "TRANSFER"
    TRANSFER_TO_OTHER_BANK = "TRANSFER_TO_OTHER_BANK"
    PAYOUT = "PAYOUT"
    PURCHASE = "PURCHASE"

    TRANSACTION_TYPES = (
        (TRANSFER, TRANSFER),
        (TRANSFER_TO_OTHER_BANK, TRANSFER_TO_OTHER_BANK),
        (PAYOUT, PAYOUT),
        (PURCHASE, PURCHASE),
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="transactions",
    )
    source_card = models.ForeignKey(
        CreditCard,
        on_delete=models.CASCADE,
        verbose_name="Источник",
        related_name="outgoing_transactions",
    )
    destination_card = models.ForeignKey(
        CreditCard,
        on_delete=models.CASCADE,
        verbose_name="Получатель",
        null=True,
        blank=True,
        related_name="incoming_transactions",
    )
    amount = models.FloatField(verbose_name="Сумма")
    commission = models.FloatField(verbose_name="Комиссия", default=0)
    metadata = models.JSONField(verbose_name="Метаданные", null=True, blank=True)
    transaction_type = models.CharField(
        max_length=50, verbose_name="Тип транзакции", choices=TRANSACTION_TYPES
    )

    def __str__(self):
        return f"Transaction {self.id}"

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"
