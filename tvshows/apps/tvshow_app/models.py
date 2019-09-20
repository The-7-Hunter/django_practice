from django.db import models

class TV_shows(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    release_date = models.DateField()

