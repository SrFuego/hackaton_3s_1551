# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import PublicationViewSet, PublicationKindViewSet


# Create your routers here.
publications = (
    (r"publication", PublicationViewSet),
    (r"publication_kind", PublicationKindViewSet),
)
