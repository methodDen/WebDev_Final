from rest_framework import serializers

from credit_cards.models import CreditCard
from transactions.services import add_bonuses_to_card

from .models import Transaction


class TransactionTransferSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Transaction
        fields = (
            "author",
            "source_card",
            "destination_card",
            "slug",
        )


class TransactionPaySerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Transaction
        fields = ("author", "amount")

    def create(self, validated_data):
        user = validated_data.get("author")
        amount = validated_data.get("amount")
        credit_card = CreditCard.objects.filter(user=user, is_main=True).first()
        if credit_card.balance < amount:
            raise serializers.ValidationError("Not enough balance on card")
        credit_card.balance -= amount
        add_bonuses_to_card(credit_card, amount)
        transaction_instance = Transaction.objects.create(
            author=user,
            source_card=credit_card,
            amount=amount,
            transaction_type=Transaction.PAYOUT,
        )
        return transaction_instance


class TransactionPayDetailSerializer(serializers.ModelSerializer):
    class TransactionCreditCardNestedSerializer(serializers.ModelSerializer):
        class Meta:
            model = CreditCard
            fields = (
                "id",
                "balance",
                "bonuses",
            )

    source_card = TransactionCreditCardNestedSerializer()

    class Meta:
        model = Transaction
        fields = (
            "id",
            "author",
            "source_card",
            "amount",
            "transaction_type",
        )
