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
