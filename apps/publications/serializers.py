# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import Publication, PublicationKind


# Create your serializers here.
class PublicationSerializer(ModelSerializer):
    class Meta:
        model = Publication
        fields = "__all__"


class PublicationKindSerializer(ModelSerializer):
    class Meta:
        model = PublicationKind
        fields = ("id", "name",)
