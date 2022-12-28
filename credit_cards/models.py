from django.db import models

from jusan import settings
from mixins.models import IsActiveMixin

# Create your models here.


class CreditCard(IsActiveMixin):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="credit_cards",
    )
    card_number = models.CharField(
        max_length=16, verbose_name="Номер карты", unique=True
    )
    card_holder = models.CharField(max_length=50, verbose_name="Владелец карты")
    expiration_date = models.DateField(verbose_name="Срок действия")
    cvv = models.CharField(max_length=3, verbose_name="CVV")
    balance = models.FloatField(verbose_name="Баланс", default=0)
    bonuses = models.FloatField(verbose_name="Бонусы", default=0)
    currency = models.CharField(max_length=3, verbose_name="Валюта", default="KZT")
    is_main = models.BooleanField(verbose_name="Основная", default=False)

    def __str__(self):
        return f"Credit card {self.card_number}"

    class Meta:
        verbose_name = "Кредитная карта"
        verbose_name_plural = "Кредитные карты"
        unique_together = ("card_number", "card_holder", "expiration_date", "cvv")
