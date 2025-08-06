from playwright.sync_api._generated import Page
import pytest
from pages.registration_page import RegistrationPage
from faker import Faker

def test_registration_with_invalid_email(page: Page):
    registration_page = RegistrationPage(page)
    registration_page.open()
    registration_page.fill_form("Test User", "invalid-email", "securepassword")
    registration_page.submit()

    error = page.locator("text=Invalid email format").is_visible()
    assert error, "Error message should be displayed for invalid email format"
    assert registration_page.has_email_validation_error(), "Email validation error should be triggered"