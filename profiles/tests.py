import pytest
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from profiles.models import Profile


@pytest.mark.django_db
class TestProfiles(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='UserTest',
            email='user_test@test.com',
            password='Abcd1234'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Paris',
        )

    def test_profiles_index(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertIn(b'<title>Profiles</title>', response.content)

    def test_profiles_detail(self):
        response = self.client.get(reverse('profiles:profile', args=["UserTest"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profiles_models(self):
        assert str(self.profile) == f'{self.profile.user.username}'
