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
