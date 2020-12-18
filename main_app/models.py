from django.db import models
from django.urls import reverse

# Create your models here.
class Potato(models.Model):
    name = models.CharField(max_length=100)
    birth_place = models.CharField(max_length=100)
    length = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField()
    description = models.TextField(max_length=250)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('potato_detail', kwargs={'potato_id': self.id})

