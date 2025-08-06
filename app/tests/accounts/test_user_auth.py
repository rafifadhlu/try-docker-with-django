from django.test import TestCase, Client
# from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.urls import reverse

class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='admin', password='rafi1234')
        
    def test_login_success(self):
        response = self.client.post(reverse("account:index"),{"username":"admin","password":"rafi1234"})
        self.assertEqual(response['Location'],reverse("index"))

    def test_login_non_user(self):
        response = self.client.post(reverse("account:index"),{"username":"nonuser","password":"wrongpass"})
        self.assertEqual(response['Location'],reverse("account:register"))

    def test_logout_user(self):
        self.client.login(username='admin', password='rafi1234')
        response = self.client.post(reverse("account:logout"))
        self.assertEqual(response['Location'], reverse("index"))


class RegisterUserTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.Userdata = {
            'username': 'testaccount',
            'password': 'rafi1234',
            'email': 'testaccount12@gmail.com'
        }

    def test_register_user(self):
        response = self.client.post(reverse("account:register"),self.Userdata)
        self.assertEqual(response['Location'], reverse("account:index"))