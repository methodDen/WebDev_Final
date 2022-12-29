from django.urls import path

from transactions.views import TransactionViewSet

urlpatterns = [
    path(
        "transfer/",
        TransactionViewSet.as_view(
            {"post": "transfer"},
        ),
        name="transfer",
    ),
    path(
        "pay/",
        TransactionViewSet.as_view(
            {"post": "pay"},
        ),
        name="pay",
    ),
    path(
        "transactions/my/<int:transaction_id>/",
        TransactionViewSet.as_view(
            {
                "get": "retrieve",
            },
            lookup_url_kwarg="transaction_id",
        ),
        name="my-transaction",
    ),
    path(
        "transactions/my/",
        TransactionViewSet.as_view(
            {
                "get": "list_transactions",
            },
        ),
        name="my-transactions",
    ),
]
