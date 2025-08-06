import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_redirect_to_dashboard(driver):
    driver.get("http://example.com/login")
    driver.find_element(By.NAME, "email").send_keys("user@example.com")
    driver.find_element(By.NAME, "password").send_keys("securepassword")
    driver.find_element(By.ID, "login-button").click()

    assert "dashboard" in driver.current_url, "User should be redirected to the dashboard after login"



# ---------------------------------------------------------------------------------------------------------------------------


from faker import Faker
fake = Faker()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)  # Wait for elements to be available
    yield driver
    driver.quit()

def test_registration_redirect_to_welcome_page(driver):
    driver.get("http://example.com/register")
    driver.find_element(By.NAME, "name").send_keys(fake.name())
    driver.find_element(By.NAME, "email").send_keys(fake.email())
    driver.find_element(By.NAME, "password").send_keys("securepassword")
    driver.find_element(By.ID, "register-button").click()


    wait= WebDriverWait(driver, 10)
    wait.until(EC.url_contains("welcome"))
    wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Registration Successful"))

    assert "welcome" in driver.current_url, "User should be redirected to the welcome page after registration"
    assert "Registration successful" in driver.page_source, "Registration success message should be displayed"



# ---------------------------------------------------------------------------------------------------------------------------


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)  # Wait for elements to be available
    yield driver
    driver.quit()




class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.NAME, "name")
        self.email_input = (By.NAME, "email")
        self.password_input = (By.NAME, "password")
        self.register_button = (By.ID, "register-button")

    def enter_name(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_register(self):
        self.driver.find_element(*self.register_button).click()
    
    def is_registration_successful(self):
        return "Registration successful" in self.driver.page_source and "welcome" in self.driver.current_url

def test_registration_with_page_object(driver):
    driver.get("http://example.com/register")
    
    registration_page = RegistrationPage(driver)
    registration_page.enter_name(fake.name())
    registration_page.enter_email(fake.email())
    registration_page.enter_password("securepassword")
    registration_page.click_register()

    assert "welcome" in driver.current_url, "User should be redirected to the welcome page after registration"
    assert "Registration successful" in driver.page_source, "Registration success message should be displayed"