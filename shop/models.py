from django.db import models
from polymorphic.models import PolymorphicModel

from jusan import settings
from mixins.models import IsActiveMixin, TimestampMixin


class Category(TimestampMixin, IsActiveMixin):
    name = models.CharField(max_length=50, verbose_name="Название")
    photo = models.URLField(verbose_name="Фото", null=True, blank=True)

    def __str__(self):
        return f"Category {self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Item(PolymorphicModel, TimestampMixin, IsActiveMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=500, blank=True, verbose_name="Описание")
    price = models.PositiveIntegerField(verbose_name="Цена")
    brand = models.CharField(max_length=100, verbose_name="Бренд")
    category = models.ManyToManyField(
        Category, verbose_name="Категория", related_name="items"
    )

    def __str__(self):
        return f"Item {self.name}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ItemPhoto(models.Model):
    photo = models.URLField(max_length=150, verbose_name="Фото")
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, verbose_name="Товар", related_name="photos"
    )

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


class Jewelry(Item):
    JEWELRY_ITEM_CHOICES = (
        ("ring", "Кольцо"),
        ("earring", "Серьга"),
        ("necklace", "Ожерелье"),
        ("watch", "Часы"),
        ("bracelet", "Браслет"),
        ("other", "Другое"),
    )
    material = models.CharField(max_length=50, verbose_name="Материал")
    weight = models.PositiveIntegerField(verbose_name="Вес")
    height = models.FloatField(verbose_name="Высота", null=True, blank=True)
    width = models.FloatField(verbose_name="Ширина", null=True, blank=True)
    length = models.FloatField(verbose_name="Длина", null=True, blank=True)
    country = models.CharField(max_length=50, verbose_name="Страна")
    color = models.CharField(max_length=50, verbose_name="Цвет", blank=True, null=True)
    item_type = models.CharField(
        verbose_name="Тип",
        max_length=50,
        choices=JEWELRY_ITEM_CHOICES,
        blank=True,
        null=True,
    )
    note = models.TextField(
        max_length=500, blank=True, verbose_name="Примечание", null=True
    )

    def __str__(self):
        return f"Jewelry {self.name}"

    class Meta:
        verbose_name = "Украшение"
        verbose_name_plural = "Украшения"


class Smartphone(Item):
    OS_CHOICES = (
        ("android", "Android"),
        ("ios", "iOS"),
        ("windows", "Windows"),
        ("other", "Другое"),
    )
    os = models.CharField(
        max_length=50, verbose_name="Операционная система", choices=OS_CHOICES
    )
    diagonal_size = models.FloatField(verbose_name="Размер диагонали")
    color = models.CharField(max_length=50, verbose_name="Цвет", blank=True, null=True)
    ram = models.PositiveIntegerField(verbose_name="Оперативная память")
    memory = models.PositiveIntegerField(verbose_name="Встроенная память")
    camera = models.PositiveIntegerField(verbose_name="Камера")
    battery_capacity = models.PositiveIntegerField(verbose_name="Емкость аккумулятора")

    def __str__(self):
        return f"Smartphone {self.name}"

    class Meta:
        verbose_name = "Смартфон"
        verbose_name_plural = "Смартфоны"


class Furniture(Item):
    FURNITURE_ITEM_CHOICES = (
        ("chair", "Стул"),
        ("table", "Стол"),
        ("bed", "Кровать"),
        ("sofa", "Диван"),
        ("other", "Другое"),
    )
    material = models.CharField(max_length=50, verbose_name="Материал")
    height = models.FloatField(verbose_name="Высота", null=True, blank=True)
    width = models.FloatField(verbose_name="Ширина", null=True, blank=True)
    length = models.FloatField(verbose_name="Длина", null=True, blank=True)
    color = models.CharField(max_length=50, verbose_name="Цвет", blank=True, null=True)
    item_type = models.CharField(
        verbose_name="Тип",
        max_length=50,
        choices=FURNITURE_ITEM_CHOICES,
        blank=True,
        null=True,
    )
    note = models.TextField(
        max_length=500, blank=True, verbose_name="Примечание", null=True
    )

    def __str__(self):
        return f"Furniture {self.name}"

    class Meta:
        verbose_name = "Мебель"
        verbose_name_plural = "Мебель"


class ItemReview(models.Model):
    text = models.TextField(max_length=500, verbose_name="Текст", blank=True, null=True)
    amount = models.PositiveIntegerField(verbose_name="Количество")
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, verbose_name="Товар", related_name="reviews"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="reviews",
    )

    def __str__(self):
        return f"Review {self.text}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
