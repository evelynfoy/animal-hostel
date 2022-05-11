from django.test import TestCase
from .models import AnimalType


class TestModels(TestCase):

    def test_animal_type_creation(self):
        animal_type = AnimalType(code='Cat', description='Cat')
        self.assertEqual(str(animal_type), 'Cat - Cat')
