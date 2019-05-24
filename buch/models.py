from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.



class Buch(models.Model):
    author = models.ForeignKey('Autoren', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    sprache = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    ausleiher = models.ForeignKey('Ausleiher', on_delete=models.CASCADE)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Autoren(models.Model):
    Name = models.CharField(max_length=200)
    Vorname = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    

class Ausleiher(models.Model):
    Name = models.CharField(max_length=200)
    Vorname = models.CharField(max_length=200)
    PLZ = models.CharField(max_length=200)
    Stadt = models.CharField(max_length=200)
    Straße = models.CharField(max_length=200)
    Land = models.CharField(max_length=200)
    Telefon = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
