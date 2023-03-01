from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Account
from django.contrib.gis.geos import Point

class UserAccountsTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.account = Account.objects.create(user=self.user, 
                                              home_address='123 Main St', 
                                              phone_number='555-1234', 
                                              location='POINT(-77.0366 38.8977)')
        
        self.user1 = User.objects.create_user(username='testuser1', password='testpass1')
        self.account = Account.objects.create(user=self.user1,
                                              home_address='48 Some St', 
                                              phone_number='555-65467', 
                                              location='POINT(22.0366 33.8977)')
    
    def test_register(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'new##pass12345',
            'password2': 'new##pass12345',
            'home_address': '456 Elm St',
            'phone_number': '555-5678',
            'location': 'POINT(-77.0437 38.9072)'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Account.objects.count(), 3)
    
    
        
    def test_edit_account(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('edit_account'), {
            'home_address': '123 Main St',
            'phone_number': '555-1234',
            'location': 'POINT(-77.0366 38.8951)'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        self.user.refresh_from_db()
        self.assertEqual(self.user.account.home_address, '123 Main St')
        self.assertEqual(self.user.account.phone_number, '555-1234')
        self.assertEqual(self.user.account.location.x, -77.0366)
        self.assertEqual(self.user.account.location.y, 38.8951)
    
    def test_map(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        accounts = response.context.get('accounts')

        self.assertEqual(accounts[0].user.username, 'testuser')
        self.assertEqual(accounts[0].home_address, '123 Main St')
        self.assertEqual(accounts[0].phone_number, '555-1234')
        self.assertEqual(accounts[0].location.x, -77.0366)
        self.assertEqual(accounts[0].location.y, 38.8977)

        self.assertEqual(accounts[1].user.username, 'testuser1')
        self.assertEqual(accounts[1].home_address, '48 Some St')
        self.assertEqual(accounts[1].phone_number, '555-65467')
        self.assertEqual(accounts[1].location.x, 22.0366)
        self.assertEqual(accounts[1].location.y, 33.8977)


    def test_account(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '123 Main St')
        self.assertContains(response, '555-1234')
        self.assertContains(response, 'POINT (-77.0366 38.8977)')



