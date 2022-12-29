from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Transaction
from .serializers import (
    TransactionDetailSerializer,
    TransactionListSerializer,
    TransactionPayDetailSerializer,
    TransactionPaySerializer,
    TransactionTransferDetailSerializer,
    TransactionTransferSerializer,
)


# Create your views here.
class TransactionViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.action == "list_transactions":
            return Transaction.objects.filter(author=self.request.user).order_by(
                "-created_at"
            )
        if self.action == "retrieve":
            transaction_id = self.kwargs[self.lookup_url_kwarg]
            return (
                Transaction.objects.filter(author=self.request.user, id=transaction_id)
                .select_related(
                    "author",
                    "source_card",
                    "destination_card",
                )
                .select_related("author__profile")
                .only(
                    "id",
                    "author__profile__first_name",
                    "author__profile__last_name",
                    "source_card__card_number",
                    "destination_card__card_number",
                    "amount",
                    "transaction_type",
                    "commission",
                )
                .first()
            )

    def get_serializer_class(self):
        if self.action == "pay":
            return TransactionPaySerializer
        if self.action == "transfer":
            return TransactionTransferSerializer
        if self.action == "list_transactions":
            return TransactionListSerializer
        if self.action == "retrieve":
            return TransactionDetailSerializer

    @action(methods=("POST",), detail=False)
    def transfer(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(TransactionTransferDetailSerializer(instance).data)

    @action(methods=("POST",), detail=False)
    def pay(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(TransactionPayDetailSerializer(instance).data)

    @action(methods=("GET",), detail=False)
    def list_transactions(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
