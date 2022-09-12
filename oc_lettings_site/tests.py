from django.test import TestCase
from django.urls import reverse


class TestHomePage(TestCase):
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn(b'<title>Holiday Homes</title>', response.content)
