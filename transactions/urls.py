from django.urls import path

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
        "transactions/my/",
        TransactionViewSet.as_view(
            {
                "get": "list",
            },
        ),
        name="credit-card",
    ),
]
