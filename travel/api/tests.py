from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

from booking.models import Profile, Hotel

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()


class ProfileAPITestCase(APITestCase):

    def setUp(self):
        user = User(username='testuser', email='test@test.com')
        user.set_password("verystrongpassword")
        user.save()

        profile = Profile.objects.create(user=user, name="testprofile")
        hotel = Hotel.objects.create(profile=profile, name='testhotel')

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_profile(self):
        profile_count = Profile.objects.count()
        self.assertEqual(profile_count, 1)

    def test_get_list(self):
        data = {}
        url = api_reverse('api_v1:profile-create')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_item(self):
        data = {"name": "another test profile"}
        url = api_reverse('api_v1:profile-create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_item(self):
        profile = Profile.objects.first()
        data = {}
        url = profile.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_item(self):
        profile = Profile.objects.first()
        url = profile.get_api_url()

        data = {"name": "another test profile"}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_item_with_auth(self):
        """
        Testing when user is authenticated.
        """
        hotel = Hotel.objects.first()
        url = hotel.get_api_url()
        data = {"name": "another test travel"}
        user = User.objects.first()
        payload = payload_handler(user)
        token = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_item(self):
        user = User.objects.first()
        payload = payload_handler(user)
        token = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        data = {"name": "another test travel"}
        url = api_reverse('api_v1:travel-create')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_login(self):
        data = {
            'username': 'testuser',
            'password': 'verystrongpassword'
        }

        url = api_reverse('api_login')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
