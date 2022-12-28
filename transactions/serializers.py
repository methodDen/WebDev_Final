from rest_framework import serializers

from credit_cards.models import CreditCard
from transactions.services import add_bonuses_to_card

from .models import Transaction


class TransactionTransferSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    source_card = serializers.CharField()
    destination_card = serializers.CharField()
    amount = serializers.FloatField()
    metadata = serializers.JSONField(required=False, allow_null=True)

    class Meta:
        model = Transaction
        fields = (
            "author",
            "source_card",
            "destination_card",
            "amount",
            "metadata",
        )

    def create(self, validated_data):
        user = validated_data.get("author")
        amount = validated_data.get("amount")
        source_card_number = validated_data.get("source_card")
        destination_card_number = validated_data.get("destination_card")

        if source_card_number == destination_card_number:
            raise serializers.ValidationError("Cannot transfer to the same card")

        source_card = CreditCard.objects.filter(
            user=user, card_number=source_card_number
        ).first()
        destination_card = CreditCard.objects.filter(
            card_number=destination_card_number
        ).first()

        if source_card.balance < amount:
            raise serializers.ValidationError("Not enough balance on card")
        source_card.balance -= amount
        if not destination_card:
            source_card.balance -= Transaction.COMMISSION
            source_card.save()
            transaction_instance = Transaction.objects.create(
                author=user,
                source_card=source_card,
                amount=amount,
                transaction_type=Transaction.TRANSFER_TO_OTHER_BANK,
                commission=Transaction.COMMISSION,
            )
            return transaction_instance

        destination_card.balance += amount
        source_card.save()
        destination_card.save()
        transaction_instance = Transaction.objects.create(
            author=user,
            source_card=source_card,
            destination_card=destination_card,
            amount=amount,
            transaction_type=Transaction.TRANSFER,
        )
        return transaction_instance


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
