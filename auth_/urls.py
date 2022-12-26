from django.urls import path

from .views import ProfileViewSet

urlpatterns = [
    path(
        "profiles/me/",
        ProfileViewSet.as_view({"get": "retrieve", "put": "update"}),
        name="profile",
    ),
]
