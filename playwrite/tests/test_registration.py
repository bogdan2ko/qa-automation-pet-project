import pytest
from pages.registration_page import RegistrationPage
from faker import Faker

fake = Faker() 



def test_registration_with_page_object(page):
    registration_page = RegistrationPage(page)
    registration_page.open()
    registration_page.fill_form(fake.name(), fake.email(), "securepassword")
    registration_page.submit()

    assert registration_page.is_registration_successful(), "Registration should be successful and redirect to welcome page"