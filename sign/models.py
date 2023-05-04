from django.db import models

# Create your models here.

class SignImages(models.Model):
    image = models.ImageField(null=True, blank=True)

