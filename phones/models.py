from django.db import models
import csv



class Phone(models.Model):
    name = models.TextField()
    price = models.PositiveIntegerField()
    image = models.TextField()
    release_date = models.TextField()
    lte_exists = models.TextField()
    slug = models.TextField()

    # def __self__(self) -> str:
    #     return f'{self.name} ({self.price} руб.)'
