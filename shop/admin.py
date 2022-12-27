from django.contrib import admin
from django.contrib.admin import ModelAdmin

from shop.models import Category, Furniture, ItemPhoto, ItemReview, Jewelry, Smartphone

# Register your models here.


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    ordering = ("id",)


@admin.register(ItemPhoto)
class ItemPhotoAdmin(ModelAdmin):
    list_display = ("id",)


@admin.register(Jewelry)
class JewelryAdmin(ModelAdmin):
    list_display = ("id", "name")


@admin.register(Smartphone)
class SmartphoneAdmin(ModelAdmin):
    list_display = ("id", "name")


@admin.register(Furniture)
class FurnitureAdmin(ModelAdmin):
    list_display = ("id", "name")


@admin.register(ItemReview)
class ItemReviewAdmin(ModelAdmin):
    list_display = (
        "id",
        "user",
    )
