# Generated by Django 3.1.7 on 2022-05-24 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='type',
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 24, 14, 34, 35, 249138)),
        ),
        migrations.AlterField(
            model_name='journal',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 24, 14, 34, 35, 249138)),
        ),
    ]