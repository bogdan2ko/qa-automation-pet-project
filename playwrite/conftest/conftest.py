import pytest
from faker import Faker

fake = Faker()

@pytest.fixture()
def generate_fake_data():
    """Fixture to generate fake data for tests."""
    return {
        "name": fake.name(),
        "email": fake.email(),
        "password": "securepassword"
    }