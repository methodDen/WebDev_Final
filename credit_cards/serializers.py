from rest_framework import serializers

from credit_cards.models import CreditCard
from credit_cards.selectors import get_credit_cards_count


class CreditCardCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CreditCard
        fields = (
            "user",
            "card_number",
            "card_holder",
            "expiration_date",
            "cvv",
        )

    def validate(self, attrs):

        if len(attrs["card_number"]) != 16:
            raise serializers.ValidationError("Card number must be 16 digits long")
        if len(attrs["cvv"]) != 3:
            raise serializers.ValidationError("CVV must be 3 digits long")
        return attrs

    def create(self, validated_data):
        user = validated_data["user"]
        card_holder = validated_data["card_holder"].upper()
        card_number = validated_data["card_number"]
        expiration_date = validated_data["expiration_date"]
        cvv = validated_data["cvv"]

        credit_cards_count = get_credit_cards_count(user.id)

        if credit_cards_count == 0:
            credit_card = CreditCard.objects.create(
                user=user,
                card_number=card_number,
                card_holder=card_holder,
                expiration_date=expiration_date,
                cvv=cvv,
                is_main=True,
            )
            return credit_card

        credit_card = CreditCard.objects.create(
            user=user,
            card_number=card_number,
            card_holder=card_holder,
            expiration_date=expiration_date,
            cvv=cvv,
        )

        return credit_card


class CreditCardDetailedResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = (
            "id",
            "card_number",
            "card_holder",
            "expiration_date",
            "cvv",
            "balance",
            "bonuses",
            "currency",
            "is_main",
        )


class CreditCardShortResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = (
            "id",
            "card_number",
            "balance",
            "bonuses",
            "currency",
            "is_main",
        )


class CreditCardSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ("is_main",)

    def update(self, instance, validated_data):
        CreditCard.objects.filter(user=instance.user).update(is_main=False)
        return super().update(instance, validated_data)
