# Generated by Django 5.0.6 on 2024-06-25 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="discount_until",
            field=models.DateField(default=datetime.date.today),
        ),
    ]
