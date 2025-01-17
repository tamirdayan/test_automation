
# Playwright Test Suite in Python

## **Overview**
This is a QA automation test suite built with Playwright for Python. It validates core functionalities of the [Sauce Labs Demo Web App](https://www.saucedemo.com), including login, navigation, and form validation, along with additional improvements to enhance test coverage and maintainability.

---

## **Features**
1. **Login Tests**:
   - Successful login with valid credentials.
   - Validation for empty input fields.
2. **Navigation Tests**:
   - Verify that navigation links redirect to the correct pages.
   - Ensure the navigation bar remains accessible across pages.
3. **Form Validation Tests**:
   - Validate error messages for invalid inputs.
   - Ensure successful form submission with valid data.
4. **Environment Variable Management**:
   - All sensitive data (e.g., credentials, URLs) is stored in a `.env` file.
5. **Data-Driven Testing**:
   - Tests are parameterized for login and form validation scenarios.
6. **HTML Report Generation**:
   - View detailed test results in an HTML report.
7. **Page Object Model (POM)**:
   - All page-specific logic is encapsulated in dedicated page classes for modularity and reusability.

---

## **Project Structure**
```
saucedemo_tester/
├── assets/                     # Placeholder for additional static resources
├── pages/                      # Page Object Model implementation
│   ├── __init__.py             # Marks the directory as a Python package
│   ├── cart_page.py            # Cart page interactions
│   ├── checkout_complete_page.py # Checkout complete page interactions
│   ├── checkout_step_one_page.py # Checkout step one page interactions
│   ├── checkout_step_two_page.py # Checkout step two page interactions
│   ├── inventory_page.py       # Inventory page interactions
│   └── login_page.py           # Login page interactions
│
├── tests/                      # Test cases
│   ├── __init__.py             # Marks the directory as a Python package
│   ├── test_login.py           # Login functionality tests
│   ├── test_navigation.py      # Navigation bar tests
│   └── test_form_validation.py # Form validation tests
│
├── .env                        # Environment variables file
├── config.py                   # Configuration and environment variable loader
├── requirements.txt            # Dependencies for the project
├── README.md                   # Project documentation
└── report.html                 # Generated HTML report
```

---

## **Installation and Setup**

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd saucedemo_tester
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # For MacOS/Linux
   venv\Scripts\activate      # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright Browsers**:
   ```bash
   playwright install
   ```

5. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add the following:
   ```plaintext
   BASE_URL=https://www.saucedemo.com
   VALID_USERNAME=standard_user
   VALID_PASSWORD=secret_sauce
   INVALID_USERNAME=invalid_user
   INVALID_PASSWORD=wrong_password
   ```

---

## **Running the Tests**

1. **Run All Tests**:
   ```bash
   pytest
   ```

2. **Run a Specific Test File**:
   ```bash
   pytest tests/test_login.py
   ```

3. **Run Tests with HTML Report**:
   Install `pytest-html`:
   ```bash
   pip install pytest-html
   ```

   Generate the HTML report:
   ```bash
   pytest --html=report.html
   ```

   Open the report in your browser:
   ```bash
   open report.html  # For MacOS/Linux
   start report.html # For Windows
   ```

---

## **Changes and Highlights**

- **Enhanced Test Coverage**:
  - Added comprehensive parameterized tests for all combinations of valid, invalid, and missing credentials in `test_login.py` and `test_form_validation.py`.
- **Improved Structure**:
  - Adopted the **Page Object Model (POM)** for better modularity, with dedicated page classes for `LoginPage`, `InventoryPage`, and others.
- **Environment Variable Enhancements**:
  - Extracted constants like `EXPECTED_ERROR_MESSAGES` and `BASE_URL` to configuration files for cleaner and maintainable code.
- **New Pages Added**:
  - Introduced `cart_page.py`, `checkout_step_one_page.py`, `checkout_step_two_page.py`, and `checkout_complete_page.py` for expanded functionality.
- **Improved Test Fixtures**:
  - Simplified setup and teardown of browser contexts using `@pytest.fixture(scope="class", autouse=True)`.
- **HTML Reporting**:
  - Enhanced reporting capabilities with `pytest-html`.

---

## **Dependencies**
- Python 3.7 or higher
- `playwright`
- `pytest`
- `python-dotenv`
- `pytest-html` (optional, for HTML reports)

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## **Suggestions for Improvement**
- **Add More Tests**: Expand the suite to cover additional scenarios (e.g., cart operations, sort items, total cost, checkout data, checkout flow).
- **Product Bugs / Gaps**: Currently the website supports only error validation of missing fields of the checkout form. Add invalid values when implemented.
- **Mock APIs**: Implement API response mocking to simulate various backend behaviors.
- **CI/CD Integration**: Integrate the suite with a CI/CD pipeline using GitHub Actions, Jenkins, etc.
- **Cross-Browser Testing**: Extend the tests to run across multiple browsers (Chromium, Firefox, WebKit).

---

Feel free to reach out for any clarifications or additional support. Happy testing! 🎉

---
Author: Tamir Dayan

tamirda@gmail.com 