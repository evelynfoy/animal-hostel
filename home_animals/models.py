''' Models '''
from django.db import models
from cloudinary.models import CloudinaryField


class AnimalType(models.Model):
    ''' Animal Type Model '''
    code = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.code)


class Animal(models.Model):
    ''' Animal Model '''
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.ForeignKey(AnimalType, on_delete=models.CASCADE,
                             related_name="home_animals_animals")
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    slogan = models.TextField(blank=True)

    class Meta:
        ''' Order alphabetically by name '''
        ordering = ['name']

    def __str__(self):
        return str(self.name)
