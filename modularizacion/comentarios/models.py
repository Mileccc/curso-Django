from django.db import models


class Comment(models.Model):

    name = models.CharField(max_length=50, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000, null=True)
    date = models.DateField(null=True)
    signature = models.CharField(max_length=30, default="Firma")

    def __str__(self):
        return self.name
