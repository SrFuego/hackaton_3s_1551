# Python imports


# Django imports


# Third party apps imports
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


# Local imports
from .models import Publication, PublicationKind
from .serializers import PublicationSerializer, PublicationKindSerializer


# Create your viewsets here.
class PublicationViewSet(ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(
            interest_areas__in=request.user.investigator.interest_areas.all())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PublicationKindViewSet(ModelViewSet):
    serializer_class = PublicationKindSerializer
    queryset = PublicationKind.objects.all()
    http_method_names = ["get"]
