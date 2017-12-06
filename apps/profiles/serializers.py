# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import InterestArea, Investigator


# Create your serializers here.
class InterestAreaSerializer(ModelSerializer):
    class Meta:
        model = InterestArea
        fields = ("id", "name", "image",)


class InvestigatorSerializer(ModelSerializer):
    class Meta:
        model = Investigator
        fields = (
            "id", "graduated", "orcid_code", "role", "unmsm_code", "user",
            "interest_areas",)
        depth = 1
