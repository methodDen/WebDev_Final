from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from auth_.models import MainUser, Profile

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
            "slug",
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


class ItemBaseSerializer(serializers.ModelSerializer):
    class PhotoNestedSerializer(serializers.ModelSerializer):
        class Meta:
            model = ItemPhoto
            fields = (
                "id",
                "photo",
            )

    photos = PhotoNestedSerializer(many=True)

    class Meta:
        model = Item
        fields = (
            "id",
            "name",
            "description",
            "price",
            "brand",
            "photos",
        )


class JewelrySerializer(ItemBaseSerializer):
    class Meta:
        model = Jewelry
        fields = ItemBaseSerializer.Meta.fields + (
            "weight",
            "height",
            "width",
            "length",
            "item_type",
        )


class SmartphoneSerializer(ItemBaseSerializer):
    class Meta:
        model = Smartphone
        fields = ItemBaseSerializer.Meta.fields + (
            "os",
            "diagonal_size",
            "ram",
            "memory",
            "camera",
            "battery_capacity",
        )


class FurnitureSerializer(ItemBaseSerializer):
    class Meta:
        model = Furniture
        fields = ItemBaseSerializer.Meta.fields + (
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


class ReviewUserNestedSerializer(serializers.ModelSerializer):
    class ProfileNestedSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = (
                "first_name",
                "last_name",
            )

    profile = ProfileNestedSerializer()

    class Meta:
        model = MainUser
        fields = ("id", "profile")


class ItemReviewSerializer(serializers.ModelSerializer):
    user = ReviewUserNestedSerializer()

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
