from credit_cards.models import CreditCard

amount_bonuses_dict = {
    50000: 0.1,
    20000: 0.05,
    5000: 0.01,
    2000: 0.005,
}


def add_bonuses_to_card(credit_card: CreditCard, amount: int):
    for amount_limit, bonus_percent in amount_bonuses_dict.items():
        if amount > amount_limit:
            credit_card.bonuses += amount * bonus_percent
            break

    credit_card.save()
