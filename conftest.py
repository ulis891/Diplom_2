import pytest
from faker import Faker
from api_client import ApiClient

fake = Faker()


@pytest.fixture
def user_data():
    return {
        "email": fake.email(),
        "password": fake.password(length=8),
        "name": fake.first_name()
    }


@pytest.fixture
def create_user(user_data):
    response = ApiClient.register_user(user_data)
    '''
    Иногда, Faker возвращает email, который уже зарегистрирован в системе.
    '''
    while response.status_code != 200:
        if response.status_code == 403:
            user_data["email"] = fake.email()
            response = ApiClient.register_user(user_data)
    yield {
        "user_data": user_data,
        "access_token": response.json().get("accessToken"),
        "response": response
    }
    if response.status_code == 200:
        token = response.json().get("accessToken")
        ApiClient.delete_user(token)


@pytest.fixture
def get_ingredients():
    return ApiClient.get_ingredients().json()


@pytest.fixture
def create_user_with_order(create_user, get_ingredients):
    token = create_user["access_token"]
    ingredients = get_ingredients["data"]
    selected_ingredients = ingredients[:2]
    orde_data = {"ingredients": selected_ingredients}
    ApiClient.create_order(token, orde_data)
    return token
