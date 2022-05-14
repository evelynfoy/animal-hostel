'''  Test Views '''
from django.test import TestCase


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
