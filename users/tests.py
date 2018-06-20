from django.contrib.auth.models import User
from django.test import TestCase

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
        	'id': '123',
            'username': 'username',
            'password': 'password'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/users', self.credentials, follow=True)
       	user = User.objects.get(pk=self.credentials["id"])
       	print("""
       		ID: {}
       		Username: {}
       		Password: {}
       		Active: {}
       		""".format(self.credentials["id"],self.credentials["username"],self.credentials["password"],response.context.is_active))
        # should be logged in now
        self.assertTrue(user.is_authenticated)

