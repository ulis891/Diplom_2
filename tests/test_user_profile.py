import pytest
import allure
from api_client import ApiClient
from data import Messages as msg


@allure.suite("Тесты изменения данных пользователя")
@allure.feature("Профиль пользователя")
class TestUserProfile:

    @allure.title("Изменение данных пользователя с авторизацией")
    @allure.description("Тест изменения любого поля профиля авторизованным пользователем")
    # @pytest.mark.parametrize("field,new_value", [
    #     ("name", "New Test Name"),
    #     ("email", "newemail@example.com")
    # ])
    @pytest.mark.parametrize("field", ["email", "name"])
    def test_update_user_data_with_auth_success(self, create_user, field):
        token = create_user["access_token"]
        user_data = create_user["user_data"]
        new_value = "new" + user_data[field]
        update_data = {field: new_value}
        response = ApiClient.update_user_data(token, update_data)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["success"] == True
        assert response_data["user"][field] == new_value

    @allure.title("Изменение данных пользователя без авторизации")
    @allure.description("Тест изменения любого поля профиля не авторизованным пользователем")
    @pytest.mark.parametrize("field", ["email", "name"])
    def test_update_user_data_invalid_token_fail(self, create_user, field):
        token = None
        user_data = create_user["user_data"]
        new_value = "new" + user_data[field]
        update_data = {field: new_value}
        response = ApiClient.update_user_data(token, update_data)
        response_data = response.json()
        assert response.status_code == 401
        assert response_data["success"] == False
        assert msg.UNAUTHORIZED in response_data["message"]
