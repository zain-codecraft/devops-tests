from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestRegisterPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get("http://localhost:3000/register")  

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_form_loads_correctly(self):
        """Verify that the registration form loads with all required fields."""
        try:
            self.assertTrue(self.driver.find_element(By.NAME, "username"))
            self.assertTrue(self.driver.find_element(By.NAME, "email"))
            self.assertTrue(self.driver.find_element(By.NAME, "password"))
            self.assertTrue(self.driver.find_element(By.NAME, "confirmPassword"))
            print("Test Passed: Registration form loaded correctly.")
        except AssertionError:
            print("Test Failed: Some form fields are missing.")
            raise

    def test_successful_registration(self):
        """Test the successful registration flow."""
        try:
            self.driver.find_element(By.NAME, "username").clear()
            self.driver.find_element(By.NAME, "username").send_keys("testuser")

            self.driver.find_element(By.NAME, "email").clear()
            self.driver.find_element(By.NAME, "email").send_keys("testuser@example.com")

            self.driver.find_element(By.NAME, "password").clear()
            self.driver.find_element(By.NAME, "password").send_keys("password123")

            self.driver.find_element(By.NAME, "confirmPassword").clear()
            self.driver.find_element(By.NAME, "confirmPassword").send_keys("password123")

            self.driver.find_element(By.NAME, "submit").click()

            WebDriverWait(self.driver, 10).until(
            EC.url_contains("/account")
            )

            self.assertIn("/account", self.driver.current_url)
            print("Test Passed: Successful registration.")
        except AssertionError:
            print("Test Failed: Registration was not successful.")
            raise

    def test_missing_fields(self):
        """Submit the form with missing fields and check default validation messages."""
        try:
            self.driver.find_element(By.NAME, "username").clear()
            self.driver.find_element(By.NAME, "email").clear()
            self.driver.find_element(By.NAME, "password").clear()
            self.driver.find_element(By.NAME, "confirmPassword").clear()
            self.driver.find_element(By.NAME, "submit").click()

            # Log the validation messages
            invalid_elements = self.driver.find_elements(By.CSS_SELECTOR, "input:invalid")
            for elem in invalid_elements:
                print(f"Invalid element: {elem.get_attribute('name')}")

            print("Test Passed: Validation message for missing fields appeared.")
        except Exception as e:
            print("Test Failed: Error occurred when testing missing fields.")
            print(e)
            raise

    def test_invalid_email(self):
        """Submit the form with an invalid email and log the error message."""
        try:
            self.driver.find_element(By.NAME, "email").send_keys("invalid-email")
            self.driver.find_element(By.NAME, "submit").click()

            # Log the validation message for invalid email
            invalid_elements = self.driver.find_elements(By.CSS_SELECTOR, "input:invalid")
            for elem in invalid_elements:
                print(f"Invalid element: {elem.get_attribute('name')}")

            print("Test Passed: Validation message for invalid email appeared.")
        except Exception as e:
            print("Test Failed: Error occurred when testing invalid email.")
            print(e)
            raise

    def test_password_mismatch(self):
        """Submit the form with mismatched passwords and log the error message."""
        try:
            self.driver.find_element(By.NAME, "password").send_keys("password123")
            self.driver.find_element(By.NAME, "confirmPassword").send_keys("password321")
            self.driver.find_element(By.NAME, "submit").click()

            # Log the validation message for mismatched passwords
            invalid_elements = self.driver.find_elements(By.CSS_SELECTOR, "input:invalid")
            for elem in invalid_elements:
                print(f"Invalid element: {elem.get_attribute('name')}")

            print("Test Passed: Validation message for password mismatch appeared.")
        except Exception as e:
            print("Test Failed: Error occurred when testing password mismatch.")
            print(e)
            raise

class TestLoginPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get("http://localhost:3000/login")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_form_loads_correctly(self):
        """Verify that the login form loads with all required fields."""
        try:
            self.assertTrue(self.driver.find_element(By.NAME, "email"))
            self.assertTrue(self.driver.find_element(By.NAME, "password"))
            self.assertTrue(self.driver.find_element(By.NAME, "submit"))
            print("Test Passed: Login form loaded correctly.")
        except AssertionError:
            print("Test Failed: Some form fields are missing.")
            raise

    def test_successful_login(self):
        """Test the successful login flow."""
        try:
            self.driver.find_element(By.NAME, "email").clear()
            self.driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
            self.driver.find_element(By.NAME, "password").clear()
            self.driver.find_element(By.NAME, "password").send_keys("password123")
            self.driver.find_element(By.NAME, "submit").click()

            # Wait for successful login (e.g., redirection to dashboard or account page)
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/")  # Adjust this based on your app's URL
            )
            self.assertIn("/", self.driver.current_url)
            print("Test Passed: Successful login.")
        except AssertionError:
            print("Test Failed: Login was not successful.")
            raise

    def test_incorrect_credentials(self):
        """Test login with incorrect credentials."""
        try:
            self.driver.find_element(By.NAME, "email").clear()
            self.driver.find_element(By.NAME, "email").send_keys("wronguser@example.com")
            self.driver.find_element(By.NAME, "password").clear()
            self.driver.find_element(By.NAME, "password").send_keys("wrongpassword")
            self.driver.find_element(By.NAME, "submit").click()

            # Wait for error message to appear
            invalid_elements = self.driver.find_elements(By.CSS_SELECTOR, "input:invalid")
            for elem in invalid_elements:
                print(f"Invalid element: {elem.get_attribute('name')}")
            print("Test Passed: Incorrect credentials error displayed.")
        except Exception as e:
            print("Test Failed: Error occurred when testing incorrect credentials.")
            print(e)
            raise

    def test_empty_fields(self):
        """Test submitting the login form with empty fields."""
        try:
            self.driver.find_element(By.NAME, "email").clear()
            self.driver.find_element(By.NAME, "password").clear()
            self.driver.find_element(By.NAME, "submit").click()

            # Wait for validation error
            invalid_elements = self.driver.find_elements(By.CSS_SELECTOR, "input:invalid")
            for elem in invalid_elements:
                print(f"Invalid element: {elem.get_attribute('name')}")
            print("Test Passed: Empty fields error displayed.")
        except Exception as e:
            print("Test Failed: Error occurred when testing empty fields.")
            print(e)
            raise

    def test_invalid_email(self):
        """Test submitting the form with an invalid email format."""
        try:
            self.driver.find_element(By.NAME, "email").clear()
            self.driver.find_element(By.NAME, "email").send_keys("invalid-email")
            self.driver.find_element(By.NAME, "password").clear()
            self.driver.find_element(By.NAME, "password").send_keys("password123")
            self.driver.find_element(By.NAME, "submit").click()

            # Wait for validation error
            invalid_elements = self.driver.find_elements(By.CSS_SELECTOR, "input:invalid")
            for elem in invalid_elements:
                print(f"Invalid element: {elem.get_attribute('name')}")
            print("Test Passed: Invalid email error displayed.")
        except Exception as e:
            print("Test Failed: Error occurred when testing invalid email.")
            print(e)
            raise

# Create a combined test suite to run both test classes together
if __name__ == "__main__":
    # Load both test classes
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRegisterPage))
    suite.addTest(unittest.makeSuite(TestLoginPage))

    # Run the suite
    unittest.TextTestRunner().run(suite)
