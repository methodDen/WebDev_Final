from rest_framework import serializers
from auth_.models import MainUser, Profile


class MainUserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('first_name', 'last_name',)


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('id', 'email', 'first_name', 'last_name', 'date_joined', 'is_staff', 'photo')


class ProfileSerializer(serializers.ModelSerializer):
    hobbies = serializers.ListField(child=serializers.CharField())
    skills = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date', 'hobbies', 'skills', 'place_of_study', 'course')


# class ProfileFullSerializer(serializers.ModelSerializer):
#     class Meta(ProfileSerializer.Meta):
#         fields = ProfileSerializer.Meta.fields +


class MainUserWithProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = MainUser
        fields = ('id', 'email', 'first_name', 'last_name', 'date_joined', 'photo', 'profile')


class ProfileBriefDescriptionSerializer(serializers.Serializer):
    brief_description = serializers.CharField()


class MainUserBriefSerializer(serializers.ModelSerializer):
    profile = ProfileBriefDescriptionSerializer()

    class Meta:
        model = MainUser
        fields = ('id', 'first_name', 'last_name', 'photo', 'profile')