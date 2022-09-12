import pytest

from django.test import TestCase
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.mark.django_db
class TestLettings(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            number=4,
            street='Street Name',
            city='City Name',
            state='FR',
            zip_code=99999,
            country_iso_code='FRA'
        )
        self.letting = Letting.objects.create(
            title="Test Letting",
            address=self.address
        )

    def test_lettings_index_view(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertIn(b'<title>Lettings</title>', response.content)

    def test_lettings_detail(self):
        response = self.client.get(reverse('lettings:letting', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')

    def test_lettings_models(self):
        assert str(self.address) == f'{self.address.number} {self.address.street}'
        assert str(self.letting) == f'{self.letting.title}'
