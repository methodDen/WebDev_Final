from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from credit_cards.models import CreditCard
from credit_cards.serializers import (
    CreditCardCreateSerializer,
    CreditCardDetailedResponseSerializer,
    CreditCardSelectSerializer,
    CreditCardShortResponseSerializer,
)


# Create your views here.
class CreditCardViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "create":
            return CreditCardCreateSerializer
        if self.action == "list":
            return CreditCardShortResponseSerializer
        if self.action == "retrieve":
            return CreditCardDetailedResponseSerializer
        if self.action == "select":
            return CreditCardSelectSerializer

    def get_queryset(self):
        if self.action == "list":
            return CreditCard.objects.filter(user=self.request.user).only(
                "id", "card_number", "balance", "bonuses", "currency", "is_main"
            )
        if self.action in ("retrieve", "select"):
            credit_card_id = self.kwargs[self.lookup_url_kwarg]
            return CreditCard.objects.filter(
                user=self.request.user, id=credit_card_id
            ).first()
        return CreditCard.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(CreditCardDetailedResponseSerializer(instance).data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=("PATCH",), detail=True)
    def select(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
