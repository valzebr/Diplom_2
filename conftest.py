import pytest
import allure
from faker import Faker

from data import register_user, delete_user, create_order

# функция генерации фэйковых валидных данных
@pytest.fixture(scope='function')
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

@pytest.fixture(scope='function')
def generate_user(generating_fake_valid_data_to_create_user):
    creds = generating_fake_valid_data_to_create_user
    return creds


@allure.step('Регистрируем пользователя с последующим удалением')
@pytest.fixture(scope='function')
def user(generate_user):
    response = register_user(generate_user)
    access_token = response.json()['accessToken']
    yield generate_user, access_token
    delete_user(access_token)

@allure.step('Создание заказа')
@pytest.fixture
def order(user):
    user_data, access_token = user
    create_order(access_token)