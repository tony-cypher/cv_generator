from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    summary = models.TextField(max_length=2000)
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    previous_work = models.TextField(max_length=500)
    skills = models.TextField(max_length=500)

    def __str__(self):
        return self.name