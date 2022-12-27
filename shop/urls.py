from django.urls import path

from shop.views import CategoryViewSet, ItemViewSet, ReviewViewSet

urlpatterns = [
    path(
        "catalog/",
        CategoryViewSet.as_view(
            {"get": "list"},
        ),
        name="categories",
    ),
    path(
        "items/",
        ItemViewSet.as_view(
            {"get": "list"},
        ),
        name="items",
    ),
    path(
        "items/<int:item_id>/",
        ItemViewSet.as_view({"get": "retrieve"}, lookup_url_kwarg="item_id"),
        name="item",
    ),
    path(
        "items/<int:item_id>/reviews/",
        ReviewViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            },
            lookup_url_kwarg="item_id",
        ),
        name="item-reviews",
    ),
]
