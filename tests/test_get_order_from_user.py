import pytest
import requests
import allure
from conftest import user, Endpoints

class TestGetOrders:

    @allure.title('Получение заказа авторизованным пользователем')
    def test_get_orders_with_auth(self, user):
        generate_user, access_token = user
        response = requests.get(Endpoints.orders_api, headers={"Authorization": access_token})

        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Получение заказа без авторизации')
    def test_get_orders_without_auth(self):
        response = requests.get(Endpoints.orders_api)

        assert response.status_code == 401
        assert response.json()['success'] is False
        assert response.json()['message'] == "You should be authorised"