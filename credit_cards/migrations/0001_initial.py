# Generated by Django 3.2.12 on 2022-12-28 09:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CreditCard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is active?"),
                ),
                (
                    "card_number",
                    models.CharField(
                        max_length=16, unique=True, verbose_name="Номер карты"
                    ),
                ),
                (
                    "card_holder",
                    models.CharField(max_length=50, verbose_name="Владелец карты"),
                ),
                ("expiration_date", models.DateField(verbose_name="Срок действия")),
                ("cvv", models.CharField(max_length=3, verbose_name="CVV")),
                ("balance", models.FloatField(default=0, verbose_name="Баланс")),
                ("bonuses", models.FloatField(default=0, verbose_name="Бонусы")),
                (
                    "currency",
                    models.CharField(
                        default="KZT", max_length=3, verbose_name="Валюта"
                    ),
                ),
                (
                    "is_main",
                    models.BooleanField(default=False, verbose_name="Основная"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="credit_cards",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Кредитная карта",
                "verbose_name_plural": "Кредитные карты",
                "unique_together": {
                    ("card_number", "card_holder", "expiration_date", "cvv")
                },
            },
        ),
    ]
