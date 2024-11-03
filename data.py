from tokenize import ContStr

import allure
import requests

from endpoints import Endpoints


@allure.step('Регистрация пользователя')
def register_user(payload):
    response = requests.post(Endpoints.register_api, data=payload)
    return response

@allure.step('Удаление пользователя')
def delete_user(access_token):
    requests.delete(Endpoints.user_api, headers={"Authorization": access_token})

@allure.step('Создание заказа авторизованным пользователем')
def create_order(order, headers=None):
    response = requests.post(Endpoints.orders_api, headers=headers, data=order)
    return response

@allure.step('Получаем список из 2х ингредиентов')
def ingredient_list():
    response = requests.get(Endpoints.ingredients_api)
    data = response.json()['data']
    return [data[i]['_id'] for i in range(2)]


class Const:
    STATUS_OK = 200
    ERROR_BAD_REQUEST = 400
    ERROR_AUTHORIZED = 401
    ERROR_STATUS_FORBIDDEN = 403
    ERROR_INTERNAL_SERVER = 500

    REASON_INTERNAL_SERVER_ERROR = 'Internal Server Error'
    REASON_UNAUTHORIZED = 'Unauthorized'
    TEXT_UNAUTHORIZED = "You should be authorised"
    TEXT_INGREDIENT_IDS_REQUIRED = "Ingredient ids must be provided"
    TEXT_USER_ALREADY_EXISTS = "User already exists"
    TEXT_REQUIRED_FIELDS_MISSING = "Email, password and name are required fields"
    TEXT_INCORRECT_CREDENTIALS = "email or password are incorrect"
