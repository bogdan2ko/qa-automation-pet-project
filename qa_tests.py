import requests
import pytest


BASE_URL = "http://example.com/api"

@pytest.fixture
def valid_credentials():
    return{
        "email": "user@example.com",
        "password": "securepassword"
    }

@pytest.fixture
def invalid_credentials():
    return {
        "email": "user@exmple.com",
        "password": "wrongpassword"
    }

def test_login_with_valid_credentials(valid_credentials):
    response=requests.post(f"{BASE_URL}/login", json=valid_credentials)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    json_data = response.json()
    assert "access_token" in json_data, "Access token not found in response"

def test_login_with_invalid_credentials(invalid_credentials):
    response= requests.post(f"{BASE_URL}/login", json=invalid_credentials)
    assert response.status_code == 401, f"Expected status code 401, got {response.status_code}"






@pytest.fixture
def valid_registration_data():
    return {
        "username": "validuser",
        "email":  "user@example.com",
        "password": "validpassword"
    }

@pytest.fixture
def invalid_registration_data():
    return {
        "username": "invaliduser",
        "email": "user@example.com",
        "password": "invalidpassword"
    }

def test_registration_with_valid_data(valid_registration_data):
    response = requests.post(f"{BASE_URL}/register", json=valid_registration_data)
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"


def test_email_already_exists(valid_registration_data):
    response = requests.post(f"{BASE_URL}/register", json=valid_registration_data)
    assert response.status_code == 409, f"Expected status code 409, got {response.status_code}"
    json_data = response.json()
    assert "Email already exists" in json_data, "Email already exists message not found in response"





