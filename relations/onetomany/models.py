# pylint: disable=invalid-str-returned
from django.db import models

# Create your models here.


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.email


class Article(models.Model):
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    headline = models.CharField(max_length=60)
    pub_date = models.DateField()

    def __str__(self):
        return self.headline
