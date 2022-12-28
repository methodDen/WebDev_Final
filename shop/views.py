from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Category, Item, ItemReview
from .serializers import (
    CategoryListSerializer,
    ItemDetailSerializer,
    ItemListSerializer,
    ItemReviewCreateSerializer,
    ItemReviewSerializer,
)


# Create your views here.
class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_class(self):
        return CategoryListSerializer


class ItemViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    permission_classes = (AllowAny,)

    filter_query_params = [
        OpenApiParameter(
            "search",
            OpenApiTypes.STR,
            description="Search by name",
        ),
    ]

    def get_queryset(self):
        if self.action == "list":
            search = self.request.query_params.get("search", None)
            queryset = Item.objects.all()
            if search:
                queryset = queryset.filter(name__icontains=search)
            return queryset
        if self.action == "retrieve":
            item_id = self.kwargs[self.lookup_url_kwarg]
            return Item.objects.prefetch_related("photos").filter(id=item_id).first()

    def get_serializer_class(self):
        if self.action == "list":
            return ItemListSerializer
        if self.action == "retrieve":
            return ItemDetailSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "category",
                OpenApiTypes.INT,
                description="Search by category",
                required=True,
            )
        ]
        + filter_query_params
    )
    def list(self, request, *args, **kwargs):
        category = self.request.query_params.get("category")
        queryset = self.get_queryset()
        queryset = queryset.filter(category=category)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ReviewViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = (AllowAny,)
        if self.action == "create":
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()

    def get_queryset(self):
        if self.action == "list":
            item_id = self.kwargs[self.lookup_url_kwarg]
            return (
                ItemReview.objects.filter(item=item_id)
                .select_related("user")
                .select_related("user__profile")
                .only(
                    "user__profile__first_name",
                    "user__profile__last_name",
                    "text",
                    "amount",
                )
            )

    def get_serializer_class(self):
        if self.action == "list":
            return ItemReviewSerializer
        if self.action == "create":
            return ItemReviewCreateSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(item_id=self.kwargs[self.lookup_url_kwarg])
        return Response(serializer.data)
