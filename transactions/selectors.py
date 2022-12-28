from credit_cards.models import CreditCard


def get_balance(user_id, credit_card_id):
    return (
        CreditCard.objects.filter(id=credit_card_id, user=user_id)
        .first()
        .only("balance")
    )
