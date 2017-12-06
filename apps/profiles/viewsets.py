# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .models import InterestArea
from .serializers import InterestAreaSerializer


# Create your viewsets here.
class InterestAreaViewSet(ModelViewSet):
    serializer_class = InterestAreaSerializer
    queryset = InterestArea.objects.all()
