from django.urls import path

from credit_cards.views import CreditCardViewSet

urlpatterns = [
    path(
        "credit-cards/",
        CreditCardViewSet.as_view(
            {"post": "create"},
        ),
        name="credit-cards",
    ),
    # path(
    #     "credit-cards/my/",
    #     CreditCardViewSet.as_view(
    #         {"get": "list"},
    #     ),
    #     name="my-credit-cards",
    # ),
    # path(
    #     "credit-cards/<int:credit_card_id>/",
    #     CreditCardViewSet.as_view(
    #         {"delete": "delete", "get": "retrieve", "patch": "select"},
    #     ),
    #     name="credit-card",
    # ),
]
