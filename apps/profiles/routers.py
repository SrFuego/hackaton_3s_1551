# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import InterestAreaViewSet


# Create your routers here.
profiles = (
    (r"interest_area", InterestAreaViewSet),
)
