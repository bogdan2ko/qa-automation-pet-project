import pytest
from pages.registration_page import RegistrationPage
from faker import Faker

fake = Faker() 

def test_registration_with_existing_email(page):
    registration_page = RegistrationPage(page)
    registration_page.open()
    registration_page.fill_form(fake.name(), "existing@mail.com", "securepassword")
    registration_page.submit()

    error = page.locator("text=Email already exists").is_visible()
    assert error, "Error message should be displayed for existing email"


