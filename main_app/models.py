from django.db import models
from django.urls import reverse
from datetime import date

WASHES = (
    ('R', 'Rinse in Sink'), 
    ('S', 'Scrub in Tub'), 
    ('D', 'Deep Soak')
)

# Create your models here.
class Accessory(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('accessories_detail', kwargs={'pk': self.id})



class Potato(models.Model):
    name = models.CharField(max_length=100)
    birth_place = models.CharField(max_length=100)
    length = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField()
    description = models.TextField(max_length=250)
    accessories = models.ManyToManyField(Accessory)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('potato_detail', kwargs={'potato_id': self.id})


class Cleaning(models.Model):
    date = models.DateField('cleaning date')
    wash = models.CharField(
        max_length=1, 
        choices=WASHES,
        default=WASHES[0][0]
    )
    potato = models.ForeignKey(Potato, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_wash_display()} on {self.date} ({self.potato.name})"

    class Meta:
        ordering = ['-date']