''' Test Models '''
from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import AnimalType, Animal, Offer


class TestModels(TestCase):
    ''' Test Models '''

    def test_animal_type_creation(self):
        ''' Tests creation of Animal Type'''
        animal_type = AnimalType(code='Cat', description='Cat')
        self.assertEqual(str(animal_type), 'Cat')

    def test_animal_creation(self):
        '''
        Tests creation of an Animal
        '''
        animal_type = AnimalType(code='Cat', description='Cat')
        animal = Animal(name='Smokey', slogan='Grey cat', slug='smokey',
                        type=animal_type,
                        description='Smokey is a perfect gentleman of a cat.')
        self.assertEqual(str(animal), 'Smokey')

    def test_offer_creation(self):
        '''
        Tests creation of an Offer
        '''
        animal_type = AnimalType(code='Cat', description='Cat')
        animal = Animal(name='Smokey', slogan='Grey cat', slug='smokey',
                        type=animal_type,
                        description='Smokey is a perfect gentleman of a cat.')
        user = User.objects.create_user(username='tom',
                                 email='tom@lyons.com',
                                 password='tommy')
        offer = Offer(slug='smokey-brian',
                      animal=animal,
                      user=user,
                      basis='F',
                      pitch='I love animals',
                      weeks=6,
                      status='P')
        self.assertEqual(str(offer), 'Smokey tom')
