from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.email
    