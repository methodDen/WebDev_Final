# Generated by Django 3.2.12 on 2022-12-27 15:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=50, verbose_name="Название")),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Item",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=500, verbose_name="Описание"
                    ),
                ),
                ("price", models.PositiveIntegerField(verbose_name="Цена")),
                ("brand", models.CharField(max_length=100, verbose_name="Бренд")),
                (
                    "category",
                    models.ManyToManyField(
                        related_name="items",
                        to="shop.Category",
                        verbose_name="Категория",
                    ),
                ),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_shop.item_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
        migrations.CreateModel(
            name="Furniture",
            fields=[
                (
                    "item_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="shop.item",
                    ),
                ),
                ("material", models.CharField(max_length=50, verbose_name="Материал")),
                (
                    "height",
                    models.FloatField(blank=True, null=True, verbose_name="Высота"),
                ),
                (
                    "width",
                    models.FloatField(blank=True, null=True, verbose_name="Ширина"),
                ),
                (
                    "length",
                    models.FloatField(blank=True, null=True, verbose_name="Длина"),
                ),
                (
                    "color",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Цвет"
                    ),
                ),
                (
                    "item_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("chair", "Стул"),
                            ("table", "Стол"),
                            ("bed", "Кровать"),
                            ("sofa", "Диван"),
                            ("other", "Другое"),
                        ],
                        max_length=50,
                        null=True,
                        verbose_name="Тип",
                    ),
                ),
                (
                    "note",
                    models.TextField(
                        blank=True, max_length=500, null=True, verbose_name="Примечание"
                    ),
                ),
            ],
            options={
                "verbose_name": "Мебель",
                "verbose_name_plural": "Мебель",
            },
            bases=("shop.item",),
        ),
        migrations.CreateModel(
            name="Jewelry",
            fields=[
                (
                    "item_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="shop.item",
                    ),
                ),
                ("material", models.CharField(max_length=50, verbose_name="Материал")),
                ("weight", models.PositiveIntegerField(verbose_name="Вес")),
                (
                    "height",
                    models.FloatField(blank=True, null=True, verbose_name="Высота"),
                ),
                (
                    "width",
                    models.FloatField(blank=True, null=True, verbose_name="Ширина"),
                ),
                (
                    "length",
                    models.FloatField(blank=True, null=True, verbose_name="Длина"),
                ),
                ("country", models.CharField(max_length=50, verbose_name="Страна")),
                (
                    "color",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Цвет"
                    ),
                ),
                (
                    "item_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ring", "Кольцо"),
                            ("earring", "Серьга"),
                            ("necklace", "Ожерелье"),
                            ("watch", "Часы"),
                            ("bracelet", "Браслет"),
                            ("other", "Другое"),
                        ],
                        max_length=50,
                        null=True,
                        verbose_name="Тип",
                    ),
                ),
                (
                    "note",
                    models.TextField(
                        blank=True, max_length=500, null=True, verbose_name="Примечание"
                    ),
                ),
            ],
            options={
                "verbose_name": "Украшение",
                "verbose_name_plural": "Украшения",
            },
            bases=("shop.item",),
        ),
        migrations.CreateModel(
            name="Smartphone",
            fields=[
                (
                    "item_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="shop.item",
                    ),
                ),
                (
                    "os",
                    models.CharField(
                        choices=[
                            ("android", "Android"),
                            ("ios", "iOS"),
                            ("windows", "Windows"),
                            ("other", "Другое"),
                        ],
                        max_length=50,
                        verbose_name="Операционная система",
                    ),
                ),
                ("diagonal_size", models.FloatField(verbose_name="Размер диагонали")),
                (
                    "color",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Цвет"
                    ),
                ),
                ("ram", models.PositiveIntegerField(verbose_name="Оперативная память")),
                (
                    "memory",
                    models.PositiveIntegerField(verbose_name="Встроенная память"),
                ),
                ("camera", models.PositiveIntegerField(verbose_name="Камера")),
                (
                    "battery_capacity",
                    models.PositiveIntegerField(verbose_name="Емкость аккумулятора"),
                ),
            ],
            options={
                "verbose_name": "Смартфон",
                "verbose_name_plural": "Смартфоны",
            },
            bases=("shop.item",),
        ),
        migrations.CreateModel(
            name="ItemReview",
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
                    "text",
                    models.TextField(
                        blank=True, max_length=500, null=True, verbose_name="Текст"
                    ),
                ),
                ("amount", models.PositiveIntegerField(verbose_name="Количество")),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="shop.item",
                        verbose_name="Товар",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отзыв",
                "verbose_name_plural": "Отзывы",
            },
        ),
        migrations.CreateModel(
            name="ItemPhoto",
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
                ("photo", models.URLField(max_length=150, verbose_name="Фото")),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="shop.item",
                        verbose_name="Товар",
                    ),
                ),
            ],
            options={
                "verbose_name": "Фото",
                "verbose_name_plural": "Фото",
            },
        ),
    ]
