import pytest
import allure
from api_client import ApiClient
from data import Messages as msg


@allure.suite("Тесты работы с заказами")
@allure.feature("Заказы")
class TestOrders:

    @allure.title("Создание заказа")
    @allure.description("Тест создания заказа авторизованным пользователем с ингредиентами")
    @pytest.mark.parametrize("ingredient_count_type", ["min", "mean", "max"])
    def test_create_order_with_auth_and_ingredients_success(self, create_user, get_ingredients, ingredient_count_type):
        token = create_user["access_token"]
        ingredients = get_ingredients["data"]
        '''В зависимости от параметра ingredient_count_type выбираем количество ингредиентов для заказа'''
        len_ingredients = len(ingredients)
        length_map = {
            "min": 1,
            "mean": len_ingredients // 2,
            "max": len_ingredients,
        }
        selected_count = length_map[ingredient_count_type]
        selected_ingredients = ingredients[:selected_count]
        payload = {"ingredients": [ing["_id"] for ing in selected_ingredients]}
        response = ApiClient.create_order(token, payload)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["success"] == True
        assert "order" in response_data
        assert "number" in response_data["order"]

    @allure.title("Создание заказа")
    @allure.description("Тест создания заказа авторизованным пользователем с ингредиентами")
    @pytest.mark.parametrize("ingredient_count_type", ["min", "mean", "max"])
    @pytest.mark.xfail(reason="По сообщению от наставника, что в этом тесте ошибка")
    def test_create_order_with_auth_and_ingredients_success(self, create_user, get_ingredients, ingredient_count_type):
        ingredients = get_ingredients["data"]
        '''В зависимости от параметра ingredient_count_type выбираем количество ингредиентов для заказа'''
        len_ingredients = len(ingredients)
        length_map = {
            "min": 1,
            "mean": len_ingredients // 2,
            "max": len_ingredients,
        }
        selected_count = length_map[ingredient_count_type]
        selected_ingredients = ingredients[:selected_count]
        payload = {"ingredients": [ing["_id"] for ing in selected_ingredients]}
        response = ApiClient.create_order(None, payload)
        response_data = response.json()
        assert response.status_code == 401
        assert response_data["success"] == False
        assert msg.UNAUTHORIZED in response_data["message"]


