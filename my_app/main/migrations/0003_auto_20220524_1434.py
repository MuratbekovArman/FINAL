# Generated by Django 3.1.7 on 2022-05-24 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220524_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 24, 14, 34, 49, 747178)),
        ),
        migrations.AlterField(
            model_name='journal',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 24, 14, 34, 49, 747178)),
        ),
    ]
