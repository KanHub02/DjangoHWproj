from django.db import models

class Dorama(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")

class Vapes(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")


class Movies(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")

# Create your models here.
