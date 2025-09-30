import requests
import allure
from data import Urls


class ApiClient:

    @staticmethod
    @allure.step("Регистрация нового пользователя")
    def register_user(user_data):
        return requests.post(Urls.REGISTER, json=user_data)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(token):
        return requests.delete(Urls.USER, headers={"Authorization": token})

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(login_data):
        return requests.post(Urls.LOGIN, json=login_data)

    @staticmethod
    @allure.step("Получение данных пользователя")
    def get_user_data(token):
        return requests.get(Urls.USER, headers={"Authorization": token})

    @staticmethod
    @allure.step("Изменение данных пользователя")
    def update_user_data(token, update_data):
        return requests.patch(
            Urls.USER,
            headers={"Authorization": token},
            json=update_data
        )

    @staticmethod
    @allure.step("Получение списка ингредиентов")
    def get_ingredients():
        return requests.get(Urls.INGREDIENTS)

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(token,order_data):
        return requests.post(Urls.ORDERS, headers={"Authorization": token}, json=order_data)

    @staticmethod
    @allure.step("Получение списка заказов пользователя")
    def get_orders(token):
        return requests.get(Urls.ORDERS, headers=token)

