# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import InterestArea, Investigator


# Register your models here.
admin.site.register(InterestArea)
admin.site.register(Investigator)
