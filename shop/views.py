from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Category, Item
from .serializers import (
    CategoryListSerializer,
    ItemDetailSerializer,
    ItemListSerializer,
)


# Create your views here.
class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = (IsAuthenticated, AllowAny)

    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_class(self):
        return CategoryListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ItemViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    permission_classes = (IsAuthenticated,)

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
            return Item.objects.filter(id=item_id).first()

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
