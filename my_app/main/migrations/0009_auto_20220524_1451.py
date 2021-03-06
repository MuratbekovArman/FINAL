# Generated by Django 3.1.7 on 2022-05-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_journal_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='num_pages',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='journal',
            name='created_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='journal',
            name='type',
            field=models.CharField(choices=[('Bt', 'Bullet'), ('Fd', 'Food'), ('Tl', 'Travel'), ('St', 'Sport')], default=None, max_length=2, null=True),
        ),
    ]
