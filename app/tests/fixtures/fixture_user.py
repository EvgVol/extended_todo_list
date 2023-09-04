import pytest


@pytest.fixture
def user_superuser(django_user_model):
    return django_user_model.objects.create_superuser(
        username='TestSuperuser',
        email='testsuperuser@todo.com',
        password='z1234567'
    )


@pytest.fixture
def user1(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUser1',
        email='testuser1@example.com',
        password='z1234567'
    )


@pytest.fixture
def user2(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUser2',
        email='testuser2@example.com',
        password='z1234567'
    )


@pytest.fixture
def token_user_superuser(user_superuser):
    from rest_framework_simplejwt.tokens import AccessToken
    token = AccessToken.for_user(user_superuser)

    return {
        'access': str(token),
    }


@pytest.fixture
def user_superuser_client(token_user_superuser):
    from rest_framework.test import APIClient

    client = APIClient()
    client.credentials(
        HTTP_AUTHORIZATION=f'Bearer {token_user_superuser["access"]}'
    )
    return client


@pytest.fixture
def token_user1(user1):
    from rest_framework_simplejwt.tokens import AccessToken
    token = AccessToken.for_user(user1)

    return {
        'access': str(token),
    }


@pytest.fixture
def user_client1(token_user1):
    from rest_framework.test import APIClient

    client = APIClient()
    client.credentials(
        HTTP_AUTHORIZATION=f'Bearer {token_user1["access"]}'
    )
    return client

@pytest.fixture
def token_user2(user2):
    from rest_framework_simplejwt.tokens import AccessToken
    token = AccessToken.for_user(user2)

    return {
        'access': str(token),
    }


@pytest.fixture
def user_client2(token_user2):
    from rest_framework.test import APIClient

    client = APIClient()
    client.credentials(
        HTTP_AUTHORIZATION=f'Bearer {token_user2["access"]}'
    )
    return client
