""" Contains Models for the home_animals app
    Three models in all
    Animal Type
    Animal
    Offer
 """
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class AnimalType(models.Model):
    """
        This is a simple model used to distinguish diffent animal types.
        Details held are just code and description
    """
    code = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.code)


class Animal(models.Model):
    """
        This model holds the details of each animal available to adopt/foster.
        Fields held are :
            Name: CharField(max_length=200, unique=True),
            slug: SlugField(max_length=200, unique=True),
            type: code from Animal Type model,
            description: TextField,
            image: CloudinaryField, defaults to placeholder
            slogan: TextField
        The list is returned ordered alphabetically.
        The str function returns the name of the animal as a string.
    """
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
        """ Returns animal name as string """
        return str(self.name)


class Offer(models.Model):
    """
        This model holds the details of each offer made on an animal.
        Fields held are :
            slug: SlugField(max_length=200, unique=True)
            animal: Animal name from Animal model
            user: Username from django User model
            basis: CharField(A- Adoption or F - Fostering)
            pitch: textarea
            status: CharField(P- Pending, A - Accepted or R - Rejected)
        The list is returned ordered alphabetically by animal name.
        The str function returns a string value of animal name + ' ' + user
        name.

    """
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
    weeks = models.PositiveSmallIntegerField(null=True, blank=True)
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
        """ Returns animal name + ' ' + username as string """
        return str(self.animal) + ' ' + str(self.user)
