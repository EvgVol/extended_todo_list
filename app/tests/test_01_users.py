import pytest


class Test01UserAPI:

    @pytest.mark.django_db(transaction=True)
    def test_01_users_not_authenticated(self, client):
        response = client.get('/api/v1/users/')

        assert response.status_code != 404, (
            'Страница `/api/v1/users/` не найдена, проверьте этот адрес в *urls.py*'
        )

        assert response.status_code == 401, (
            'Проверьте, что при GET запросе `/api/v1/users/` без токена авторизации возвращается статус 401'
        )


    @pytest.mark.django_db(transaction=True)
    def test_03_users_me_not_authenticated(self, client):
        response = client.get('/api/v1/users/me/')

        assert response.status_code != 404, (
            'Страница `/api/v1/users/me/` не найдена, проверьте этот адрес в *urls.py*'
        )

        assert response.status_code == 401, (
            'Проверьте, что при GET запросе `/api/v1/users/me/` без токена авторизации возвращается статус 401'
        )
