from django.db import models

# Create your models here.
# Name, region, price, volume, description
class Scotch(models.Model):
    name = models.CharField(max_length=100)
    scotch_regions = (
        ('HL', 'Highland'),
        ('IS', 'Islay'),
        ('LL', 'Lowland'),
        ('SS', 'Speyside'),
    )
    region = models.CharField(max_length=2, choices=scotch_regions)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    volume = models.CharField(max_length=25)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name