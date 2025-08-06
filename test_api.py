import requests
import pytest


BASE_URL = "http://example.com/api"

@pytest.fixture
def user_id():
    return 1

def test_get_user_success(user_id):
    response= requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200, "Expected status code 200"
    json_data= response.json()
    assert json_data["id"] == user_id, "User ID does not match"
    assert "email" in json_data, "Email field is missing in response"
    assert "name" in json_data, "Name field is missing in response"

def test_get_user_not_found():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404, "Expected status code 404 for non-existent user"


# --------------------------------------------------------------------------------

@pytest.fixture
def user_id():
    return 1

def test_user_delete_success(user_id):
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 204, "Expected status code 204 for successful deletion"
     


def test_get_user_not_found(user_id):
    response=requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 404, "Expected status code 404 for deleted user"
        

# --------------------------------------------------------------------------------




@pytest.fixture
def user_id():
    return 1


def test_get_users_success(user_id):
    response=requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200, "Expected status code 200 for successful retrieval"
    json_data = response.json()
    assert "email" in json_data, "Email field is missing in user data"
    assert "name" in json_data, "Name field is missing in user data"


from faker import Faker
fake = Faker()
fake1= Faker("ru_RU") 



def test_put_user_success_with_faker(user_id):
    updated_data = {
        "name" : fake1.name(),
        "email" : fake.email()
    }
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=updated_data)
    assert response.status_code == 200, "Expected status code 200 for successful update"
    assert response.json()["name"] == updated_data["name"], "Name was not updated correctly"    
    get_response = requests.get(f"{BASE_URL}/users/{user_id}")
    json_data = get_response.json()
    assert json_data["name"] == updated_data["name"], "Name does not match after update"
    assert json_data["email"] == updated_data["email"], "Email does not match after update"


def test_put_user_success(user_id):
    updated_data= {
        "name": "Updated User",
        "email": "Updated Email"
    }
    response= requests.put(f"{BASE_URL}/users/{user_id}", json=updated_data)
    json_data = response.json()
    assert json_data["name"] == updated_data["name"], "Name was not updated correctly"
    assert json_data["email"] == updated_data["email"], "Email was not updated correctly"
    assert response.status_code == 200, "Expected status code 200 for successful update"