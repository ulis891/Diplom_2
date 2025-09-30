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
    yield {
        "user_data": user_data,
        "access_token": response.json().get("accessToken"),
        "response": response
    }

    if response.status_code == 200:
        token = response.json().get("accessToken")
        if token:
            ApiClient.delete_user(token)


@pytest.fixture
def get_ingredients():
    return ApiClient.get_ingredients().json()
