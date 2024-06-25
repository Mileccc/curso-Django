# pylint: disable=invalid-str-returned
from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# RELACION UNO A UNO. models.OneToOneField (clase, on_delete=models.CASCADE, primary_key=True)


class Restaurant(models.Model):

    place = models.OneToOneField(
        Place, on_delete=models.CASCADE, primary_key=True)
    number_of_employees = models.IntegerField(default=1)

    def __str__(self):
        return self.place.name
