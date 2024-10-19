from faker import Faker
import requests
import allure
from endpoints import Endpoints


# функция генерации фэйковых валидных данных
@staticmethod
def generating_fake_valid_data_to_create_user():
    fake = Faker("ru_RU")
    email = fake.email()
    password = fake.password()
    name = fake.name()
    data = {
        "email": email,
        "password": password,
        "name": name
    }

    return data

@allure.step('Регистрация пользователя')
def register_user(payload):
    response = requests.post(Endpoints.register_api, data=payload)
    return response


@allure.step('Удаление пользователя')
def delete_user(access_token):
    requests.delete(Endpoints.user_api, headers={"Authorization": access_token})