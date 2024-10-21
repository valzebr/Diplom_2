import pytest
import requests
import allure

from data import register_user

class TestCreateUser:

    @allure.title('Создание уникального пользователя')
    def test_create_unique_user(self, generate_user):
        creds = generate_user
        response = register_user(creds)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_already_registered_user(self, user):
        generate_user, access_token = user
        response = register_user(generate_user)
        print(response.json())
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "User already exists"

    @allure.title('Создание пользователя без заполненного одного из обязательных полей')
    @pytest.mark.parametrize('empty_field', ['email', 'name', 'password'])
    def test_create_user_with_missed_field_fail(self, empty_field, generate_user):
        creds = generate_user
        del creds[empty_field]
        response = register_user(generate_user)
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"