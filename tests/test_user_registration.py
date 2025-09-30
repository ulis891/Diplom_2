import pytest
import allure
from api_client import ApiClient


@allure.epic("Тестирование API для Stellar Burgers")
@allure.suite("Тесты регистрации пользователя")
@allure.feature("Регистрация пользователя")
class TestUserRegistration:

    @allure.title("Создание уникального пользователя")
    @allure.description("Тест успешной регистрации нового пользователя с валидными данными")
    def test_create_unique_user_success(self, create_user):
        response = create_user["response"]
        user_data = create_user["user_data"]
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["success"] == True
        assert "accessToken" in response_data
        assert "refreshToken" in response_data
        assert response_data["user"]["email"] == user_data["email"]
        assert response_data["user"]["name"] == user_data["name"]

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user_fail(self, create_user):
        existing_user_data = create_user["user_data"]
        response = ApiClient.register_user(existing_user_data)
        response_data = response.json()
        assert response.status_code == 403
        assert response_data["success"] == False
        assert response_data["message"] == "User already exists"

    @allure.title("Создание пользователя без обязательного поля: {missing_field}")
    @allure.description("Тест регистрации с отсутствующим обязательным полем")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_required_field_fail(self, user_data, missing_field):
        invalid_data = user_data.copy()
        del invalid_data[missing_field]
        response = ApiClient.register_user(invalid_data)
        response_data = response.json()
        assert response.status_code == 403
        assert response_data["success"] == False
        assert "required field" in response_data["message"]
