from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


def create_users_api(user_superuser):
    data = {
        'username': 'TestUser',
        'role': 'user',
    }
    user_superuser.post('/api/v1/users/', data=data)
    user = get_user_model().objects.get(username=data['username'])
    return user


def auth_client(user):
    refresh = RefreshToken.for_user(user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client


def create_categories(user_superuser_client):
    data1 = {
        'name': 'Тестовая категория 1',
    }
    user_superuser_client.post('/api/v1/categories/', data=data1)
    data2 = {
        'name': 'Тестовая категория 2',
    }
    user_superuser_client.post('/api/v1/categories/', data=data2)
    return [data1, data2]
