import requests
import allure

from endpoints import Endpoints
from data import Const

class TestGetOrders:

    @allure.title('Получение заказа авторизованным пользователем')
    def test_get_orders_with_auth(self, user):
        generate_user, access_token = user
        response = requests.get(Endpoints.orders_api, headers={"Authorization": access_token})

        assert response.status_code == Const.STATUS_OK
        assert response.json()['success'] is True

    @allure.title('Получение заказа без авторизации')
    def test_get_orders_without_auth(self):
        response = requests.get(Endpoints.orders_api)

        assert response.status_code == Const.ERROR_AUTHORIZED
        assert response.json()['success'] is False
        assert response.json()['message'] == Const.TEXT_UNAUTHORIZED