import pytest
from .common import auth_client, create_categories, create_users_api


class Test01CategoryAPI:

    @pytest.mark.django_db(transaction=True)
    def test_01_category_not_auth(self, client):
        response = client.get('/api/v1/categories/')
        assert response.status_code != 404, (
            'Страница `/api/v1/categories/` не найдена, проверьте этот адрес в *urls.py*'
        )
        assert response.status_code == 200, (
            'Проверьте, что при GET запросе `/api/v1/categories/` без токена авторизации возвращается статус 200'
        )
