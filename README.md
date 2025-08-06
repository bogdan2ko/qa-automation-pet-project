# QA Automation Pet Project

Automation of user registration testing  
**Stack:** Python • Playwright • Pytest • Faker • Allure


## 🚀 Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

2. **Install Playwright browsers:**
    playwright install

3. **Run tests:**
    pytest


## Allure Reports

1. **Generate results:**
    pytest --alluredir=allure-results

2. **Serve the report:**
    allure serve allure-results

✅ Test Cases
✅ UI Positive: successful registration with redirect

❌ UI Negative: empty fields, invalid email, duplicate email

✅ API Positive: user creation via API

❌ API Negative: duplicate email → returns status code 409

