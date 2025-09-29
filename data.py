class Urls:

    BASE_URL = "https://stellarburgers.nomoreparties.site/api"

    # Эндпоинты авторизации
    REGISTER = f"{BASE_URL}/auth/register"
    LOGIN = f"{BASE_URL}/auth/login"
    USER = f"{BASE_URL}/auth/user"

    # Эндпоинты заказов и ингредиентов
    ORDERS = f"{BASE_URL}/orders"
    INGREDIENTS = f"{BASE_URL}/ingredients"
