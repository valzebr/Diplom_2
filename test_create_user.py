import pytest
import requests
import allure

from data import register_user, delete_user, generating_fake_valid_data_to_create_user

class TestCreateUser:

    def test_create_unique_user(self, generate_user):  # создать уникального пользователя
        creds = generate_user
        response = register_user(creds)
        assert response.status_code == 200
        assert response.json()["success"] is True

    def test_create_already_registered_user(self, user):
        # создать пользователя, который уже зарегистрирован (НЕ РАБОТАЕТ!!!)
        generate_user, access_token = user
        response = register_user(generate_user)
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "User already exists"

    def test_create_user_without_required_fields(self):
        user_data = {
            "email": "no_name@ya.ru",
            "password": "password123"
            # Отсутствует поле "name"
        }
        response = register_user(user_data)
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"


# создать пользователя и не заполнить одно из обязательных полей
