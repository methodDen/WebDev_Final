from django.urls import path

from transactions.views import TransactionViewSet

urlpatterns = [
    # path(
    #     "transfer/",
    #     TransactionViewSet.as_view(
    #         {"post": "transfer"},
    #     ),
    #     name="transfer",
    # ),
    path(
        "pay/",
        TransactionViewSet.as_view(
            {"post": "pay"},
        ),
        name="pay",
    ),
    # path(
    #     "transactions/my/",
    #     TransactionViewSet.as_view(
    #         {
    #             "get": "list",
    #         },
    #     ),
    #     name="my-transactions",
    # ),
    # path(
    #     "transactions/my/<int:transaction_id>/",
    #     TransactionViewSet.as_view(
    #         {
    #             "get": "retrieve",
    #         },
    #     ),
    #     name="my-transaction",
    # ),
]
