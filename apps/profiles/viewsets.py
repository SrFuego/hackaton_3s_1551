# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .models import InterestArea, Investigator
from .serializers import InterestAreaSerializer, InvestigatorSerializer


# Create your viewsets here.
class InterestAreaViewSet(ModelViewSet):
    serializer_class = InterestAreaSerializer
    queryset = InterestArea.objects.all()


class InvestigatorViewSet(ModelViewSet):
    serializer_class = InvestigatorSerializer
    queryset = Investigator.objects.all()
