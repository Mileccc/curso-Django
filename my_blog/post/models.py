# pylint: disable=invalid-str-returned
from django.db import models
from datetime import date


class Author(models.Model):

    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def __str__(self):

        return self.name


class Entry(models.Model):

    # Clave Foranea user --> Ponemos el nombre de la tabla a la que apunta. Apuntara al ID que automaticamente escribe.
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    bodytext = models.TextField(max_length=100)
    public_date = models.DateField(default=date.today)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
