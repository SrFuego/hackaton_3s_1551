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
    user = UserSerializer()

    class Meta:
        model = Investigator
        fields = (
            "id", "orcid_code", "role", "unmsm_code", "user",
            "interest_areas",)

    def create(self, validated_data):
        user_tmp = validated_data.pop("user")
        user = get_user_model().objects.create_user(
            user_tmp["username"], user_tmp["email"], user_tmp["password"],
            first_name=user_tmp["first_name"], last_name=user_tmp["last_name"])
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
