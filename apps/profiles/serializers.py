# Python imports


# Django imports
from django.contrib.auth import get_user_model


# Third party apps imports
from rest_framework import serializers
from rest_framework.utils import model_meta


# Local imports
from .models import InterestArea, Investigator


# Create your serializers here.
class InterestAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestArea
        fields = ("id", "name", "image",)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ("username", "password", "first_name", "last_name", "email",)


class InvestigatorSerializer(serializers.ModelSerializer):
    orcid_code = serializers.CharField(allow_null=True)
    user = UserSerializer(read_only=True)
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True, allow_blank=True)

    class Meta:
        model = Investigator
        fields = (
            "id", "orcid_code", "role", "unmsm_code", "user", "interest_areas",
            "last_name", "username", "password", "first_name", "email")

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            validated_data["username"], validated_data["email"],
            validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"])
        validated_data.pop("username")
        validated_data.pop("email")
        validated_data.pop("password")
        validated_data.pop("first_name")
        validated_data.pop("last_name")
        info = model_meta.get_field_info(Investigator)
        many_to_many = {}
        for field_name, relation_info in info.relations.items():
            if relation_info.to_many and (field_name in validated_data):
                many_to_many[field_name] = validated_data.pop(field_name)
        instance = Investigator.objects.create(user=user, **validated_data)
        if many_to_many:
            for field_name, value in many_to_many.items():
                field = getattr(instance, field_name)
                field.set(value)
        return instance
