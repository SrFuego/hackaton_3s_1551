# Python imports


# Django imports
from django.conf import settings
from django.db import models


# Third party apps imports
from model_utils.models import TimeStampedModel


# Local imports


# Create your models here.
class InterestArea(TimeStampedModel):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Area de Interes"
        verbose_name_plural = "Areas de Interes"

    def __str__(self):
        return self.name


class Investigator(TimeStampedModel):
    UNDERGRADUATE = "undergraduate"
    BACHELOR = "bachelor"
    PROFESSOR = "professor"
    POSTGRADUATE = "postgraduate"

    ROLE_CHOICES = (
        (UNDERGRADUATE, "Pregrado"),
        (BACHELOR, "Bachiller"),
        (PROFESSOR, "Docente"),
        (POSTGRADUATE, "Postgrado"),)

    graduated = models.BooleanField(default=False)
    interest_areas = models.ManyToManyField(
        "InterestArea", null=True, blank=True)
    orcid_code = models.CharField(max_length=16, blank=True)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    unmsm_code = models.CharField(max_length=8, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name = "Investigador"
        verbose_name_plural = "Investigadores"

    def __str__(self):
        return self.user.get_full_name()
