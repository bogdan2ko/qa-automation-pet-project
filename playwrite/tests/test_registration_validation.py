import pytest
from pages.registration_page import RegistrationPage

def test_registratioon_with_empty_name(page):
    registration_page = RegistrationPage(page)
    registration_page.open()
    registration_page.fill_form(name="Test User", email=" ", password="securepassword")
    registration_page.submit()

    error=page.locator("text=Email is required").is_visible()
    assert error.is_visible(), "Error message should be displayed for empty email field"
