# pylint: disable=invalid-str-returned
from django.db import models

# Create your models here.

# RELACION MUCHOS A MUCHOS
# NO hace falta la restriccion ONDELETE.ONCASCADE


class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline
