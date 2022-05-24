from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from rest_framework.permissions import IsAuthenticated


class BaseClass(models.Model):
    class Meta:
        abstract = True

    permission_classes = [IsAuthenticated]


class BookJournalBase(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0, null=True)
    description = models.CharField(max_length=600, null=True)
    created_at = models.DateTimeField(default=None, null=True)

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField(null=True)
    genre = models.CharField(max_length=200, null=True)


class Journal(BookJournalBase):
    BULLET = 'Bt'
    FOOD = 'Fd'
    TRAVEL = 'Tl'
    SPORT = 'St'
    TYPE_CHOICES = [
        (BULLET, 'Bullet'),
        (FOOD, 'Food'),
        (TRAVEL, 'Travel'),
        (SPORT, 'Sport')
    ]
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=None, null=True)
    publisher = models.CharField(max_length=400, null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)
