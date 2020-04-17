from django.db import models
from django.utils import timezone
from django.contrib import admin

class Email(models.Model):
    email = models.EmailField(null = False)

class Event(models.Model):

    event_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100)
    content = models.TextField()
    location = models.CharField(max_length=100)


    def __str__(self):
        return self.title

class Gal(models.Model):
    img = models.ImageField(verbose_name="IMAGES", upload_to="gallery_pics")
    created_at = models.DateField(default=timezone.now)

    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=5000)
    