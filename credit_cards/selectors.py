from credit_cards.models import CreditCard


def get_credit_cards_count(user_id: int) -> int:
    return CreditCard.objects.filter(user=user_id).count()
