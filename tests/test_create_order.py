import allure
import requests
from data import ingredient_list
from endpoints import Endpoints
from data import Const


class TestCreateOrder:
    @allure.title('Создание заказа авторизованным пользователем')
    def test_create_order_with_auth_success(self, user):
        user_data, access_token = user
        order = {'ingredients': ingredient_list()}
        response = requests.post(Endpoints.orders_api, headers={"Authorization": access_token}, json=order)

        assert response.status_code == Const.STATUS_OK
        assert response.json()["success"] is True
        assert 'number' in response.json()['order']

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_auth_success(self):
        order = {'ingredients': ingredient_list()}
        response = requests.post(Endpoints.orders_api, json=order)

        assert response.status_code == Const.STATUS_OK
        assert response.json()["success"] is True
        assert 'number' in response.json()['order']

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients_fail(self):
        response = requests.post(Endpoints.orders_api, json={})

        assert response.status_code == Const.ERROR_BAD_REQUEST
        assert response.json()["success"] is False
        assert response.json()["message"] == Const.TEXT_INGREDIENT_IDS_REQUIRED

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_wrong_hash_ingredients_fail(self):
        order = {'ingredients': ['wrong_hash_ingredient']}
        response = requests.post(Endpoints.orders_api, json=order)

        assert response.status_code == Const.ERROR_INTERNAL_SERVER
        assert response.reason == Const.REASON_INTERNAL_SERVER_ERROR