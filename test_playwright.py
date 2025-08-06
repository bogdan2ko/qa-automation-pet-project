
from playwright.sync_api import Page
import pytest
from faker import Faker

fake=Faker()

@pytest.mark.parametrize("password", ["securepassword"])
def test_registration_redirect_towelcome_page(page: Page, password):
    page.goto("http://example.com/register")
    page.fill("input[name='name']", fake.name())
    page.fill("input[name='email']", fake.email())
    page.fill("input[name='password']", password)
    page.click("#register-button")

    page.wait_for_url("**/welcome")

    assert "welcome" in page.url, "User should be redirected to the welcome page after registration"
    assert page.locator("text=Registration Successful").is_visible(), "Registration success message should be displayed"


# .................................................................................






class RegistrationPage():
    def __init__(self, page: Page):
        self.page = page
        self.name_input = "input[name='name']"
        self.email_input = "input[name='email']"
        self.password_input = "input[name='password']"
        self.register_button = "#register-button"

    def open(self):
        self.page.goto("http://example.com/register")
    

    def fill_form(self, name:str, email:str, password:str):
        self.page.fill(self.name_input, name)
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)

    def submit(self):
        self.page.click(self.register_button)

    def is_registration_successful(self):
        return "/welcome" in self.page.url and \
            self.page.locator("text=Registration Successful").is_visible()







 
    
def test_registration_with_page_object(page):
    registration_page = RegistrationPage(page)
    registration_page.open()
    registration_page.fill_form(fake.name(), fake.email(), "securepassword")
    registration_page.submit()

    assert registration_page.is_registration_successful(), "Registration should be successful and redirect to welcome page"
