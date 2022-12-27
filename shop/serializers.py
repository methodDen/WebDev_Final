from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from auth_.models import MainUser

from .models import (
    Category,
    Furniture,
    Item,
    ItemPhoto,
    ItemReview,
    Jewelry,
    Smartphone,
)


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "photo",
        )


class ItemListSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = (
            "id",
            "price",
            "avatar",
            "name",
        )

    def get_avatar(self, instance):
        if instance.photos.first():
            return instance.photos.first().photo
        return None


class JewelrySerializer(serializers.ModelSerializer):
    class PhotoNestedSerializer(serializers.ModelSerializer):
        class Meta:
            model = ItemPhoto
            fields = ("photo",)

    photos = PhotoNestedSerializer(many=True)

    class Meta:
        model = Jewelry
        fields = (
            "id",
            "name",
            "description",
            "price",
            "brand",
            "photos",
            "weight",
            "height",
            "width",
            "length",
            "item_type",
        )


class SmartphoneSerializer(serializers.ModelSerializer):
    class PhotoNestedSerializer(serializers.ModelSerializer):
        class Meta:
            model = ItemPhoto
            fields = ("photo",)

    photos = PhotoNestedSerializer(many=True)

    class Meta:
        model = Smartphone
        fields = (
            "id",
            "name",
            "description",
            "price",
            "brand",
            "photos",
            "os",
            "diagonal_size",
            "ram",
            "memory",
            "camera",
            "battery_capacity",
        )


class FurnitureSerializer(serializers.ModelSerializer):
    class PhotoNestedSerializer(serializers.ModelSerializer):
        class Meta:
            model = ItemPhoto
            fields = ("photo",)

    photos = PhotoNestedSerializer(many=True)

    class Meta:
        model = Furniture
        fields = (
            "id",
            "name",
            "description",
            "price",
            "brand",
            "photos",
            "material",
            "color",
            "note",
            "item_type",
        )


class ItemDetailSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Jewelry: JewelrySerializer,
        Smartphone: SmartphoneSerializer,
        Furniture: FurnitureSerializer,
    }


class ItemReviewSerializer(serializers.ModelSerializer):
    class UserNestedSerializer(serializers.ModelSerializer):
        class Meta:
            model = MainUser
            fields = ("id", "email")

    user = UserNestedSerializer()

    class Meta:
        model = ItemReview
        fields = (
            "id",
            "user",
            "amount",
            "text",
        )


class ItemReviewCreateSerializer(serializers.ModelSerializer):
    amount = serializers.IntegerField()
    text = serializers.CharField(allow_null=True, allow_blank=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ItemReview
        fields = (
            "id",
            "user",
            "amount",
            "text",
        )
