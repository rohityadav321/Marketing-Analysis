from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='teampics')
    role = models.CharField(max_length=50)
    insta = models.CharField(max_length=150)
    github = models.CharField(max_length=150)
    linkedin = models.CharField(max_length=150)
    insta = models.CharField(max_length=150)
