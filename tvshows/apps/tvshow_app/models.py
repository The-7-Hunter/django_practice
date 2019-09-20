from __future__ import unicode_literals
from django.db import models


class TV_shows_manager(models.Manager):
    def validator(self, postedData):
        errors = {}
        if len(postedData['title']) < 1:
            errors['title'] = "title cannot be empty"
        if len(postedData['network']) < 1:
            errors['network'] = "network cannot be empty"
        if len(postedData['description']) < 1:
            errors['description'] = "description cannot be empty"
        return errors

class TV_shows(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    release_date = models.DateField()
    objects = TV_shows_manager()
