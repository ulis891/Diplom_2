import pytest
import allure
from api_client import ApiClient
from data import Messages as msg


@allure.epic("Тестирование API для Stellar Burgers")
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

    @allure.title("Логин c несуществующим пользователем")
    @allure.description("Тест неуспешной авторизации с несуществующими учетными данными")
    @pytest.mark.parametrize("missing_field", ["email", "password"])
    def test_login_user_missing_required_field_fail(self, create_user, missing_field):
        user_data = create_user["user_data"]
        login_data = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        login_data[missing_field] += "_invalid"
        response = ApiClient.login_user(login_data)
        response_data = response.json()
        assert response.status_code == 401
        assert response_data["success"] == False
        assert msg.INCORRECT_LOGIN in response_data["message"]
