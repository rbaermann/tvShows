from __future__ import unicode_literals
from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = 'TV show title should be at least 2 characters'
        if len(postData['network']) < 3:
            errors['network'] = 'TV show network should be at least 3 characters'
        if len(postData['desc']) > 0 and len(postData['desc']) < 10:
            errors['desc'] = 'TV show description should be at least 10 characters'
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f'{self.title} {self.network} {self.release_date} {self.created_at} {self.updated_at}' 
