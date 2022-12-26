from rest_framework import serializers

from .models import MainUser, Profile


class UserProfileDetailedSerializer(serializers.ModelSerializer):
    class ProfileNestedSerializer(serializers.Serializer):
        first_name = serializers.CharField(max_length=30, required=False)
        last_name = serializers.CharField(max_length=30, required=False)
        photo = serializers.URLField(max_length=150, required=False)
        description = serializers.CharField(max_length=500, required=False)
        location = serializers.CharField(max_length=200, required=False)
        birth_date = serializers.DateField(required=False)

    id = serializers.IntegerField()
    email = serializers.EmailField()
    profile = ProfileNestedSerializer()

    class Meta:
        model = MainUser
        fields = (
            "id",
            "email",
            "profile",
        )


class ProfileRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "first_name",
            "last_name",
            "photo",
            "description",
            "location",
            "birth_date",
        )
