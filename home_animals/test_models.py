"""
    Contains all the tests for the home_animals application models
"""
from django.test import TestCase
from django.contrib.auth.models import User
from .models import AnimalType, Animal, Offer


class TestModels(TestCase):
    """
        Test Class for all the tests
    """

    def test_animal_type_creation(self):
        '''
            Tests creation of Animal Type
            First creates a test animal type with a set value of 'Cat'
            Then tests that the str function on the created object returns the
            same value.
        '''
        animal_type = AnimalType(code='Cat', description='Cat')
        self.assertEqual(str(animal_type), 'Cat')

    def test_animal_creation(self):
        '''
            Tests creation of an Animal object.
            First creates a test animal type with a set value of 'Cat'.
            Then creates a test animal with specific values including
            the test animal type and the name of 'Smokey'.
            Then tests that the str function on the created object returns the
            name 'Smokey'.
        '''
        animal_type = AnimalType(code='Cat', description='Cat')
        animal = Animal(name='Smokey', slogan='Grey cat', slug='smokey',
                        type=animal_type,
                        description='Smokey is a perfect gentleman of a cat.')
        self.assertEqual(str(animal), 'Smokey')

    def test_offer_creation(self):
        '''
            Tests creation of an Offer object
            Creates a test animal type with a set value of 'Cat'.
            Creates a test animal with specific values including
            the test animal type and the name of 'Smokey'.
            Creates a test user with a name of 'tom'.
            Then creates a test offer with specific values including
            the test animal type, animal and user.
            Then tests that the str function on the created object returns the
            name 'Smokey tom'.
        '''
        animal_type = AnimalType(code='Cat', description='Cat')
        animal = Animal(name='Smokey', slogan='Grey cat', slug='smokey',
                        type=animal_type,
                        description='Smokey is a perfect gentleman of a cat.')
        user = User.objects.create_user(username='tom',
                                        email='tom@lyons.com',
                                        password='tommy')
        offer = Offer(slug='smokey-tom',
                      animal=animal,
                      user=user,
                      basis='F',
                      pitch='I love animals',
                      weeks=6,
                      status='P')
        self.assertEqual(str(offer), 'Smokey tom')
