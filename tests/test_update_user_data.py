import pytest
import requests
import allure

from endpoints import Endpoints
from data import Const


class TestChangeUserData:

    @allure.title('Изменение данных пользователя с авторизацией')
    @pytest.mark.parametrize('edited_field', ['email', 'name', 'password'])
    def test_update_user_data_with_auth(self, user, edited_field, generating_fake_valid_data_to_create_user):
        user_data, access_token = user
        new_creds = generating_fake_valid_data_to_create_user
        user_data[edited_field] = new_creds[edited_field]
        response = requests.patch(Endpoints.user_api, headers={"Authorization": access_token}, json=user_data)

        assert response.status_code == Const.STATUS_OK
        assert response.json()['success'] is True
        assert 'email' in response.json()['user']
        assert 'name' in response.json()['user']

    @allure.title('Изменение данных пользователя без авторизации')
    @pytest.mark.parametrize('edited_field', ['email', 'name', 'password'])
    def test_update_user_data_without_auth(self, user, edited_field, generating_fake_valid_data_to_create_user):
        user_data, access_token = user
        new_creds = generating_fake_valid_data_to_create_user
        user_data[edited_field] = new_creds[edited_field]
        response = requests.patch(Endpoints.user_api, json=user_data)


        assert response.status_code == Const.ERROR_AUTHORIZED
        assert response.json()['success'] is False
        assert response.json()["message"] == Const.TEXT_UNAUTHORIZED