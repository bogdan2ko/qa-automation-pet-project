from playwright.sync_api import Page
from faker import Faker

fake=Faker()


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
    
    def has_email_validation_error(self):
        return self.page.locator("text=Invalid email format").is_visible()
    
    def has_empty_fields_error(self):
        return self.page.locator("text=All fields are required").is_visible()
