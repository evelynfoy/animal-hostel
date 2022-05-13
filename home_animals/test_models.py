''' Test Models '''
from django.test import TestCase
from .models import AnimalType, Animal


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
