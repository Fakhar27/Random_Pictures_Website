from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    text = models.TextField()


class contacts(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    text = models.TextField()

    def __str__(self):
        return self.name
