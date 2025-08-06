# POST http://example.com/api/register


import requests
from faker import Faker

from pages.registration_page import RegistrationPage
fake = Faker()
BASE_URL = "http://example.com/api/register"

def test_registration_api_success():
    data = {
        "name": fake.name(),
        "email": fake.email(),
        "password": "securepassword"
    }
    response= requests.post(BASE_URL, json=data)
    assert response.status_code == 201, "Registration should be successful"


def test_registration_api_duplicate_email():
    data ={
        "name": fake.name(),
        "email": fake.email(),
        "password": "securepassword"
    }

    requests.post(BASE_URL, json=data)
    response = requests.post(BASE_URL, json=data)
    assert response.status_code == 409, "Registration should fail with duplicate email"
    assert "Email already exists" in response.text, "Error message should indicate email already exists"


def test_registration_api_success_simple(generate_fake_data):
    response = requests.post(BASE_URL, json=generate_fake_data)
    assert response.status_code == 201, "Registration should be successful with generated data"
    

    
def test_registration_with_empty_fields(page):
    registration_page = RegistrationPage(page)
    registration_page.open()
    registration_page.fill_form(name="", email="", password="")
    registration_page.submit()

    error = page.locator("text=All fields are required").is_visible()
    assert error, "Error message should be displayed for empty fields"
    assert registration_page.has_empty_fields_error(), "Empty fields validation error should be triggered"