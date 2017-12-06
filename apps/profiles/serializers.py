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
        fields = "__all__"


class InvestigatorSerializer(ModelSerializer):
    class Meta:
        model = Investigator
        fields = "__all__"
