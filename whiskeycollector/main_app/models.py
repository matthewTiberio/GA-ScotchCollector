from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

TYPES = (
    ('B', 'Bourbon'),
    ('I', 'Irish'),
    ('R', 'Rye'),
    ('S', 'Scotch'),
    ('O', 'Other'),
)

# Create your models here.
class WhiskeyTypes(models.Model):
    type = models.CharField(max_length=1, choices=TYPES, default=TYPES[-1][0])
    description = models.TextField(max_length=1000)


class Whiskey(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(WhiskeyTypes, on_delete=models.CASCADE)
    origin = models.CharField(max_length=25)
    subType = models.CharField('Sub Type', max_length=25)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    volume = models.CharField(max_length=25)
    description = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'whiskey_id': self.id})

