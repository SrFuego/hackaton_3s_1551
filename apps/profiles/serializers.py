# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import InterestArea


# Create your serializers here.
class InterestAreaSerializer(ModelSerializer):
    class Meta:
        model = InterestArea
        fields = "__all__"
