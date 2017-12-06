# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Publication, PublicationKind


# Register your models here.
admin.site.register(Publication)
admin.site.register(PublicationKind)
