import pytest
import allure
from api_client import ApiClient
from data import Messages as msg, OrdersInfo as oi


@allure.epic("Тестирование API для Stellar Burgers")
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
        order_data = {"ingredients": [ing["_id"] for ing in selected_ingredients]}
        response = ApiClient.create_order(token, order_data)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["success"] == True
        assert "order" in response_data
        assert "number" in response_data["order"]

    @allure.title("Создание заказа")
    @allure.description("Тест создания заказа авторизованным пользователем с ингредиентами")
    @pytest.mark.parametrize("ingredient_count_type", ["min", "mean", "max"])
    @pytest.mark.xfail(reason="По сообщению от наставника, что в этом тесте ошибка")
    def test_create_order_with_auth_and_ingredients_success(self, get_ingredients, ingredient_count_type):
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
        order_data = {"ingredients": [ing["_id"] for ing in selected_ingredients]}
        response = ApiClient.create_order(None, order_data)
        response_data = response.json()
        assert response.status_code == 401
        assert response_data["success"] == False
        assert msg.UNAUTHORIZED in response_data["message"]

    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Тест попытки создания заказа без указания ингредиентов")
    def test_create_order_without_ingredients_fail(self, create_user):
        token = create_user["access_token"]
        order_data = {"ingredients": []}
        response = ApiClient.create_order(token, order_data)
        response_data = response.json()
        assert response.status_code == 400
        assert response_data["success"] == False
        assert msg.INGREDIENTS_FAIL in response_data["message"]

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    @allure.description("Тест создания заказа с некорректными хешами ингредиентов")
    def test_create_order_with_invalid_ingredient_hash_fail(self, create_user):
        token = create_user["access_token"]
        order_data = {"ingredients": ["invalid_hash_1", "invalid_hash_2"]}
        response = ApiClient.create_order(token, order_data)
        assert response.status_code == 500

    @allure.title("Получение заказов авторизованного пользователя")
    @allure.description("Тест получения истории заказов авторизованного пользователя")
    def test_get_user_orders_with_auth_success(self, create_user_with_order):
        token = create_user_with_order
        response = ApiClient.get_user_orders(token)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["success"] == True
        assert "orders" in response_data
        for field in oi.USER_INFO:
            assert field in response_data
        for field in oi.ORDER_INFO:
            assert field in response_data["orders"][0]

    @allure.title("Получение заказов неавторизованного пользователя")
    @allure.description("Тест получения истории заказов не авторизованного пользователя")
    def test_get_user_orders_without_auth_fail(self, create_user_with_order):
        response = ApiClient.get_user_orders(None)
        response_data = response.json()
        assert response.status_code == 401
        assert response_data["success"] == False
        assert msg.UNAUTHORIZED in response_data["message"]
