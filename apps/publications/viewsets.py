# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .models import Publication, PublicationKind
from .serializers import PublicationSerializer, PublicationKindSerializer


# Create your viewsets here.
class PublicationViewSet(ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class PublicationKindViewSet(ModelViewSet):
    serializer_class = PublicationKindSerializer
    queryset = PublicationKind.objects.all()
    http_method_names = ["get"]
