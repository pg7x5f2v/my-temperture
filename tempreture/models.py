from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Temp(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    temperture = models.FloatField()
    ##memo = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        sttemp = str(self.temperture)
        return sttemp