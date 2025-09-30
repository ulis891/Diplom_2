import pytest
import allure
from api_client import ApiClient


@allure.suite("Тесты авторизации пользователя")
@allure.feature("Логин пользователя")
class TestUserLogin:

    @allure.title("Логин под существующим пользователем")
    @allure.description("Тест успешной авторизации с валидными учетными данными")
    def test_login_existing_user_success(self, create_user):
        user_data = create_user["user_data"]
        login_data = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        response = ApiClient.login_user(login_data)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["success"] == True
        assert "accessToken" in response_data
        assert "refreshToken" in response_data
        assert response_data["user"]["email"] == user_data["email"]
        assert response_data["user"]["name"] == user_data["name"]

