# Python imports


# Django imports
from django.db import models


# Third party apps imports
from model_utils.models import TimeStampedModel


# Local imports


# Create your models here.
class PublicationKind(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Tipo de Publicacion"
        verbose_name_plural = "Tipos de Publicaciones"

    def __str__(self):
        return self.name


class Publication(TimeStampedModel):
    author = models.ManyToManyField(
        "profiles.Investigator", related_name="publications")
    description = models.TextField()
    kind = models.ForeignKey("PublicationKind", related_name="publications")
    title = models.TextField()
    interest_areas = models.ManyToManyField(
        "profiles.InterestArea", blank=True)

    class Meta:
        verbose_name = "Publicacion"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.title
