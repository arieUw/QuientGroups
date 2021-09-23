from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phoneno = models.CharField(max_length=13)
    message = models.TextField()

    def __str__(self):
        return self.name
   