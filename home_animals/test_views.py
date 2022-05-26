"""  Test Views """
from django.test import TestCase
from django.contrib.auth.models import User
from .models import AnimalType, Animal, Offer


class TestViews(TestCase):
    """  Test Views """

    def test_guest_list(self):
        """ Test Display Guest List """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_guest_list_template(self):
        """ Test Display Guest List Template"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'pages/index.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_guest_detail_view(self):
        """ Test Display Guest Detail View"""
        animal_type = AnimalType.objects.create(code='Cat',
                                                description='Cat')
        guest = Animal.objects.create(name='Test Guest',
                                      slug='test',
                                      type=animal_type,
                                      description='Test',
                                      slogan='Test')
        response = self.client.get(f'/guest/{guest.slug}/')
        self.assertEqual(response.status_code, 200)

    def test_offer_list(self):
        """ Test Display Offer List """
        response = self.client.get('/offers/')
        self.assertEqual(response.status_code, 200)

    def test_offer_list_template(self):
        """ Test Display Offer List Template"""
        response = self.client.get('/offers/')
        self.assertTemplateUsed(response, 'pages/offers.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_offer_add(self):
        """ Test Add Offer View """
        response = self.client.get('/offer/add/')
        self.assertEqual(response.status_code, 200)

    def test_offer_add_template(self):
        """ Test Display Offer List Template"""
        response = self.client.get('/offer/add/')
        self.assertTemplateUsed(response, 'pages/offer_add.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_can_add_offer(self):
        """ Test an offer can be added"""
        animal_type = AnimalType.objects.create(code='Cat', description='Cat')
        animal = Animal.objects.create(name='Smokey', slogan='Grey cat',
                                       slug='smokey',
                                       type=animal_type,
                                       description='Smokey is a perfect gentleman of a cat.')
        user = User.objects.create_user(username='tom',
                                        email='tom@lyons.com',
                                        password='tommy')
        self.client.force_login(user=user)
        response = self.client.post('/offer/add/',
                                    {'animal': ['1'],
                                     'pitch': ['fgdfh'],
                                     'basis': ['A'],
                                     'weeks': ['']})
        self.assertRedirects(response, '/offers/')

    def test_offer_edit(self):
        """ Test Edit Offer View """
        animal_type = AnimalType.objects.create(code='Cat', description='Cat')
        animal = Animal.objects.create(name='Smokey', slogan='Grey cat',
                                       slug='smokey',
                                       type=animal_type,
                                       description='Smokey is a perfect gentleman of a cat.')
        user = User.objects.create_user(username='tom',
                                        email='tom@lyons.com',
                                        password='tommy')
        offer = Offer.objects.create(slug=str(user) + "-" + animal.name,
                                     animal=animal,
                                     user=user,
                                     pitch='fgdfh',
                                     basis='F',
                                     weeks=2)
        response = self.client.get(f'/offer/edit/{offer.slug}')

    def test_offer_edit_template(self):
        """ Test Edit Offer Template"""
        animal_type = AnimalType.objects.create(code='Cat', description='Cat')
        animal = Animal.objects.create(name='Smokey', slogan='Grey cat',
                                       slug='smokey',
                                       type=animal_type,
                                       description='Smokey is a perfect gentleman of a cat.')
        user = User.objects.create_user(username='tom',
                                        email='tom@lyons.com',
                                        password='tommy')
        offer = Offer.objects.create(slug=str(user) + "-" + animal.name,
                                     animal=animal,
                                     user=user,
                                     pitch='fgdfh',
                                     basis='F',
                                     weeks=2)
        response = self.client.get(f'/offer/edit/{offer.slug}')
        self.assertTemplateUsed(response, 'pages/offer_edit.html')
        self.assertTemplateUsed(response, 'base.html')

    