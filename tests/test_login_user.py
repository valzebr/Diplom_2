import pytest
import requests
import allure
from endpoints import Endpoints


class TestLoginUser:


    @allure.title('Логин под существующим пользователем')
    def test_login_user_success(self, user):
        response = requests.post(Endpoints.login_api, data=user[0])

        assert response.status_code == 200
        assert response.json()['success'] is True
        assert 'accessToken' in response.json()
        assert 'refreshToken' in response.json()
        assert response.json()['user']['email'] == user[0]['email']
        assert response.json()['user']['name'] == user[0]['name']


    @allure.title('Логин с неверным логином и паролем')
    @pytest.mark.parametrize('wrong_field', ['email', 'password'])
    def test_login_user_fail(self, user, wrong_field):
        user[0][wrong_field] += user[0][wrong_field]
        response = requests.post(Endpoints.login_api, data=user[0])

        assert response.status_code == 401
        assert response.reason == 'Unauthorized'
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"