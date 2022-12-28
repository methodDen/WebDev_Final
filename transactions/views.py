from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import TransactionPayDetailSerializer, TransactionPaySerializer


# Create your views here.
class TransactionViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        pass

    def get_serializer_class(self):
        if self.action == "pay":
            return TransactionPaySerializer

    @action(methods=("POST",), detail=False)
    def transfer(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=("POST",), detail=False)
    def pay(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(TransactionPayDetailSerializer(instance).data)
