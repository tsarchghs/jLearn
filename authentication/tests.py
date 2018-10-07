from django.test import TestCase
from django.shortcuts import resolve_url as r
# Create your tests here.

class SignUpViewTestGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('signup'))

    def test_get(self):
        """GET Rerqust should return status code 200."""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'auth/signup.html')

    def test_html(self):
        """HTML must contains input tags."""

        tags = (
            ('<form', 2),
            ('<input', 9),
            ('type="checkbox"', 1),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="password"', 2),
            ('type="submit"', 1),
        )

        for text, count in tags:
            self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """HTML must contains csrf."""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')
