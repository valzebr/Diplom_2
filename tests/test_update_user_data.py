import pytest
import requests
import allure
from conftest import Endpoints, generating_fake_valid_data_to_create_user

@allure.title('Изменение данных пользователя с авторизацией')
@pytest.mark.parametrize("updated_data", [
    generating_fake_valid_data_to_create_user(),
    generating_fake_valid_data_to_create_user(),
])
def test_update_user_data_with_auth(user, updated_data):
    generate_user, access_token = user
    response = requests.patch(Endpoints.user_api, json=updated_data, headers={"Authorization": access_token})
    assert response.status_code == 200
    assert response.json()['user']['email'] == updated_data['email']
    assert response.json()['user']['name'] == updated_data['name']


@allure.title('Изменение данных пользователя без авторизации')
@pytest.mark.parametrize("updated_data", [
    generating_fake_valid_data_to_create_user(),
    generating_fake_valid_data_to_create_user(),
])
def test_update_user_data_without_auth(updated_data):
    response = requests.patch(Endpoints.user_api, json=updated_data)
    assert response.status_code == 401
    assert response.json()['success'] is False
    assert response.json()['message'] == "You should be authorised"