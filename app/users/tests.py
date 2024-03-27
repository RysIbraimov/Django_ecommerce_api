from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import CustomUser


class UserViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_list_users(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_user(self):
        data = {
            'username': 'newuser',
            'password': 'newpassword',
        }
        response = self.client.post(reverse('user-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_retrieve_user(self):
        detail_url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        update_data = {'username': 'updateduser'}
        detail_url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.patch(detail_url, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        detail_url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class RegisterAPIViewTestCase(APITestCase):
    def test_register_user(self):
        url = reverse('register')
        data = {
            'username': 'new_user',
            'password': 'new_password',
            'email': 'new_user@example.com'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('username' in response.data)
        self.assertEqual(response.data['username'], 'new_user')


class LoginAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')

    def test_login_user(self):
        url = reverse('login')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('refresh' in response.data)
        self.assertTrue('access' in response.data)


class LogoutAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(self.user)

    def test_logout_user(self):
        url = reverse('logout')

        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['detail'], 'Successfully logged out AnonymousUser')