""" Models """
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class AnimalType(models.Model):
    """ Animal Type Model """
    code = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.code)


class Animal(models.Model):
    """ Animal Model """
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.ForeignKey(AnimalType, on_delete=models.CASCADE,
                             related_name="home_animals_animals")
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    slogan = models.TextField(blank=True)

    class Meta:
        """ Order alphabetically by name """
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Offer(models.Model):
    """ Offer Model """
    slug = models.SlugField(max_length=200, unique=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE,
                               related_name="home_animals_animal")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="home_animals_user")
    ADOPTION = 'A'
    FOSTERING = 'F'
    OFFER_CHOICES = [
        (ADOPTION, 'Adoption'),
        (FOSTERING, 'Fostering'),
    ]
    basis = models.CharField(
        max_length=1,
        choices=OFFER_CHOICES)
    pitch = models.TextField()
    weeks = models.IntegerField(null=True, blank=True)
    APPROVED = 'A'
    PENDING = 'P'
    REJECTED = 'R'
    STATUS_CHOICES = [
        (APPROVED, 'Aproved'),
        (PENDING, 'Pending'),
        (REJECTED, 'Rejected'),
    ]
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES)

    class Meta:
        """ Order alphabetically by name """
        ordering = ['animal']

    def __str__(self):
        return str(self.animal) + ' ' + str(self.user)
