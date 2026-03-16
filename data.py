class Urls:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"

    # Эндпоинты авторизации
    REGISTER = f"{BASE_URL}/auth/register"
    LOGIN = f"{BASE_URL}/auth/login"
    USER = f"{BASE_URL}/auth/user"

    # Эндпоинты заказов и ингредиентов
    ORDERS = f"{BASE_URL}/orders"
    INGREDIENTS = f"{BASE_URL}/ingredients"


class Messages:
    INCORRECT_LOGIN = "email or password are incorrect"
    UNAUTHORIZED = "You should be authorised"
    INGREDIENTS_FAIL = "Ingredient ids must be provided"


class OrdersInfo:
    ORDER_INFO = ["_id", "ingredients", "status", "name", "createdAt", "updatedAt", "number"]
    USER_INFO = ["success", "orders", "total", "totalToday"]
