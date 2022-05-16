'''  Test Views '''
from django.test import TestCase
from .models import AnimalType, Animal
from django.shortcuts import render, redirect, get_object_or_404


class TestViews(TestCase):
    '''  Test Views '''

    def test_guest_list(self):
        ''' Test Display Guest List '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_guest_list_template(self):
        ''' Test Display Guest List Template'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_guest_detail_view(self):
        ''' Test Display Guest Detail View'''
        animal_type = AnimalType.objects.create(code='Cat',  description='Cat')
        guest = Animal.objects.create(name='Test Guest', slug='test', type=animal_type, description='Test', slogan='Test')
        print(guest.id)

        response = self.client.get(f'guest_detail/{guest.slug}')
        # # response = self.client.get(f'/guest_detail/{guest.id}')
        self.assertEqual(response.status_code, 200)
        

