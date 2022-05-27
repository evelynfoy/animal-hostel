"""
    Contains all the tests views for the home_animals application
"""
from django.test import TestCase
from django.contrib.auth.models import User
from .models import AnimalType, Animal, Offer


class TestViews(TestCase):
    """
        Test Class for all the tests
    """

    def test_guest_list(self):
        """
            Tests rendering of home page or Guest List view
            Checks that a status of 200 is received on requesting the home
            page.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_guest_list_template(self):
        """
            Tests templates rendered for home page or Guest List view.
        """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'pages/index.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_guest_detail_view(self):
        """
            Tests rendering of Guest Detail view.
            First creates a test animal type with a set value of 'Cat'.
            Then creates a test animal with specific values including
            the test animal type and a slug value of 'test'.
            Then checks that a status of 200 is received on requesting the
            Guest Detail template passing in the slug for this animal
        """
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
        """
            Tests rendering of 'offers/' url.
            Checks that a status of 200 is received on requesting this
            url.
        """
        response = self.client.get('/offers/')
        self.assertEqual(response.status_code, 200)

    def test_offer_list_template(self):
        """
            Tests templates rendered for 'offers/' url.
        """
        response = self.client.get('/offers/')
        self.assertTemplateUsed(response, 'pages/offers.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_offer_add(self):
        """
            Tests rendering of 'offers/add' url.
            Checks that a status of 200 is received on requesting this
            url.
        """
        response = self.client.get('/offer/add/')
        self.assertEqual(response.status_code, 200)

    def test_offer_add_template(self):
        """
            Tests templates rendered for 'offers/add/' url.
            Checks that a status of 200 is received on requesting this
            url.
        """
        response = self.client.get('/offer/add/')
        self.assertTemplateUsed(response, 'pages/offer_add.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_can_add_offer(self):
        """
            Tests that an offer entry can be added using the 'offer/add/ url.
            Creates a test animal type with a set value of 'Cat'.
            Creates a test animal.
            Creates a user.
            Logs on as this user.
            Then checks that a status of 200 is received on requesting the
            post function for the 'offer/add/' url passing an object with offer
            details for the test animal.
        """
        animal_type = AnimalType.objects.create(code='Cat', description='Cat')
        animal = Animal.objects.create(name='Smokey', slogan='Grey cat',
                                       slug='smokey',
                                       type=animal_type,
                                       description='Test description')
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
        """
            Tests rendering of 'offers/edit' url.
            Creates a test animal type with a set value of 'Cat'.
            Creates a test animal.
            Creates a user.
            Ceates a test offer.
            Then checks that a status of 200 is received on requesting this
            url passing the slug of the test animal..
        """
        animal_type = AnimalType.objects.create(code='Cat', description='Cat')
        animal = Animal.objects.create(name='Smokey', slogan='Grey cat',
                                       slug='smokey',
                                       type=animal_type,
                                       description='Test description.')
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
        self.assertEqual(response.status_code, 200)

    def test_offer_edit_template(self):
        """
            Tests templates rendered for 'offers/edit' url.
            Creates a test animal type with a set value of 'Cat'.
            Creates a test animal.
            Creates a user.
            Ceates a test offer.
            Then checks the templates used on requesting this
            url passing the slug of the test animal.
        """
        animal_type = AnimalType.objects.create(code='Cat', description='Cat')
        animal = Animal.objects.create(name='Smokey', slogan='Grey cat',
                                       slug='smokey',
                                       type=animal_type,
                                       description='Test description.')
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

    def test_can_edit_offer(self):
        """
            Tests that an offer entry can be edited using the 'offer/edit/'
            url.
            Creates a test animal type with a set value of 'Cat'.
            Creates a test animal.
            Creates a test user.
            Creates a test offer.
            Logs on as this user.
            Then it requests the 'offer/edit/' url passing in the slug for the
            test offer and an object containing test change details (pitch=
            'changed').
            Then it checks that the response is redirection to the 'offers/'
            url.
            Then the test offer is retrieved from the database and tested to
            see if the value for pitch is in fact now equal to 'changed'.
        """
        animal_type = AnimalType.objects.create(code='Cat', description='Cat')
        animal = Animal.objects.create(name='Smokey', slogan='Grey cat',
                                       slug='smokey',
                                       type=animal_type,
                                       description='Test description.')
        user = User.objects.create_user(username='tom',
                                        email='tom@lyons.com',
                                        password='tommy')
        offer = Offer.objects.create(slug=str(user) + "-" + animal.name,
                                     animal=animal,
                                     user=user,
                                     pitch='fgdfh',
                                     basis='F',
                                     weeks=2)
        self.client.force_login(user=user)
        response = self.client.post(f'/offer/edit/{offer.slug}',
                                    {'animal': ['1'],
                                     'pitch': ['changed'],
                                     'basis': ['A'],
                                     'weeks': ['']})
        self.assertRedirects(response, '/offers/')
        updated_offer = Offer.objects.get(slug=offer.slug)
        self.assertEqual(updated_offer.pitch, 'changed')

    def test_offer_delete(self):
        """
            Tests rendering of 'offers/delete' url.
            Creates a test animal type with a set value of 'Cat'.
            Creates a test animal.
            Creates a user.
            Ceates a test offer.
            Then checks that a status of 200 is received on requesting this
            url passing the slug of the test animal..
        """
        animal_type = AnimalType.objects.create(code='Cat', description='Cat')
        animal = Animal.objects.create(name='Smokey', slogan='Grey cat',
                                       slug='smokey',
                                       type=animal_type,
                                       description='Test description.')
        user = User.objects.create_user(username='tom',
                                        email='tom@lyons.com',
                                        password='tommy')
        offer = Offer.objects.create(slug=str(user) + "-" + animal.name,
                                     animal=animal,
                                     user=user,
                                     pitch='fgdfh',
                                     basis='F',
                                     weeks=2)
        response = self.client.get(f'/offer/delete/{offer.slug}')
        self.assertEqual(response.status_code, 200)

    def test_offer_delete_template(self):
        """
            Tests templates rendered for 'offers/delete' url.
            Creates a test animal type with a set value of 'Cat'.
            Creates a test animal.
            Creates a user.
            Ceates a test offer.
            Then checks the templates used on requesting this
            url passing the slug of the test animal.
        """
        animal_type = AnimalType.objects.create(code='Cat', description='Cat')
        animal = Animal.objects.create(name='Smokey', slogan='Grey cat',
                                       slug='smokey',
                                       type=animal_type,
                                       description='Test description.')
        user = User.objects.create_user(username='tom',
                                        email='tom@lyons.com',
                                        password='tommy')
        offer = Offer.objects.create(slug=str(user) + "-" + animal.name,
                                     animal=animal,
                                     user=user,
                                     pitch='fgdfh',
                                     basis='F',
                                     weeks=2)
        response = self.client.get(f'/offer/delete/{offer.slug}')
        self.assertTemplateUsed(response, 'pages/offer_delete.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_can_delete_offer(self):
        """
            Tests that an offer entry can be deleted using the 'offer/delete/'
            url.
            Creates a test animal type with a set value of 'Cat'.
            Creates a test animal.
            Creates a test user.
            Creates a test offer.
            Logs on as this user.
            Then it requests the 'offer/delete/' url passing in the slug for
            the test offer.
            Then it checks that the response is redirection to the 'offers/'
            url.
            Then any offers existing in the database for the test slug are
            retrieved and the test checks that the length of this list is 0.
        """
        animal_type = AnimalType.objects.create(code='Cat', description='Cat')
        animal = Animal.objects.create(name='Smokey', slogan='Grey cat',
                                       slug='smokey',
                                       type=animal_type,
                                       description='Test description.')
        user = User.objects.create_user(username='tom',
                                        email='tom@lyons.com',
                                        password='tommy')
        offer = Offer.objects.create(slug=str(user) + "-" + animal.name,
                                     animal=animal,
                                     user=user,
                                     pitch='fgdfh',
                                     basis='F',
                                     weeks=2)
        self.client.force_login(user=user)
        response = self.client.post(f'/offer/delete/{offer.slug}')
        self.assertRedirects(response, '/offers/')
        existing_offers = Offer.objects.filter(slug=offer.slug)
        self.assertEqual(len(existing_offers), 0)
