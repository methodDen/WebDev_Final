from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import MainUser, Profile
from .serializers import ProfileRequestSerializer, UserProfileDetailedSerializer


# Create your views here.
class ProfileViewSet(
    viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin
):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.action == "retrieve":
            return (
                MainUser.objects.filter(id=self.request.user.id)
                .select_related("profile")
                .only(
                    "id",
                    "email",
                    "profile__id",
                    "profile__first_name",
                    "profile__last_name",
                    "profile__avatar",
                    "profile__description",
                    "profile__location",
                    "profile__birth_date",
                    "profile__phone",
                )
                .first()
            )
        return Profile.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserProfileDetailedSerializer
        if self.action == "update":
            return ProfileRequestSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_queryset().first()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
