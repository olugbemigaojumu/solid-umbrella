"""Register User on automationexercise.com (test case: sign up, verify, delete the account)"""
import time

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://automationexercise.com/"

# Unique email per run so the signup never collides with an existing account
STAMP = int(time.time())
USER = {
    "name": "TestUser",
    "email": f"test_user_{STAMP}@example.com",
    "password": "Test@12345",
    "dob_day": "15",
    "dob_month": "May",
    "dob_year": "1992",
    "first_name": "Test",
    "last_name": "User",
    "company": "Test Company",
    "address1": "123 Test Street",
    "address2": "Apartment 4B",
    "country": "United States",
    "state": "California",
    "city": "Los Angeles",
    "zipcode": "90001",
    "mobile": "1234567890",
}


def build_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Blocks most ad iframes that otherwise intercept clicks on this site
    options.add_argument("--disable-popup-blocking")
    return webdriver.Chrome(options=options)


def dismiss_consent(driver):
    """The site sometimes shows a cookie-consent dialog; close it if present."""
    try:
        btn = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-cta-consent")))
        btn.click()
    except TimeoutException:
        pass


def safe_click(driver, locator, timeout=10):
    """Click normally; if an ad overlay intercepts the click, fall back to a JS click."""
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    try:
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator)).click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", element)


def visible(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))


def main():
    driver = build_driver()
    try:
        # 1-2. Launch browser, navigate to URL
        driver.get(URL)
        dismiss_consent(driver)

        # 3. Verify the home page is visible
        assert "Automation Exercise" in driver.title, f"Unexpected title: {driver.title!r}"
        visible(driver, (By.CSS_SELECTOR, "img[alt='Website for automation practice']"))
        print("Home page is visible.")

        # 4. Click 'Signup / Login'
        safe_click(driver, (By.CSS_SELECTOR, "a[href='/login']"))

        # 5. Verify 'New User Signup!'
        heading = visible(driver, (By.CSS_SELECTOR, ".signup-form h2"))
        assert heading.text.strip() == "New User Signup!", f"Got: {heading.text!r}"
        print("'New User Signup!' is visible.")

        # 6-7. Enter name + email, click Signup
        driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']").send_keys(USER["name"])
        driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys(USER["email"])
        safe_click(driver, (By.CSS_SELECTOR, "button[data-qa='signup-button']"))

        # 8. Verify 'ENTER ACCOUNT INFORMATION'
        heading = visible(driver, (By.CSS_SELECTOR, "h2.title.text-center b"))
        assert heading.text.strip().upper() == "ENTER ACCOUNT INFORMATION", f"Got: {heading.text!r}"
        print("'ENTER ACCOUNT INFORMATION' is visible.")

        # 9. Title, name, email, password, date of birth
        safe_click(driver, (By.ID, "id_gender1"))  # Mr.
        name_field = driver.find_element(By.ID, "name")
        assert name_field.get_attribute("value") == USER["name"]  # pre-filled from signup
        email_field = driver.find_element(By.ID, "email")
        assert email_field.get_attribute("value") == USER["email"]
        driver.find_element(By.ID, "password").send_keys(USER["password"])
        Select(driver.find_element(By.ID, "days")).select_by_value(USER["dob_day"])
        Select(driver.find_element(By.ID, "months")).select_by_visible_text(USER["dob_month"])
        Select(driver.find_element(By.ID, "years")).select_by_value(USER["dob_year"])

        # 10-11. Newsletter + special offers checkboxes
        safe_click(driver, (By.ID, "newsletter"))
        safe_click(driver, (By.ID, "optin"))
        assert driver.find_element(By.ID, "newsletter").is_selected()
        assert driver.find_element(By.ID, "optin").is_selected()

        # 12. Address details
        driver.find_element(By.ID, "first_name").send_keys(USER["first_name"])
        driver.find_element(By.ID, "last_name").send_keys(USER["last_name"])
        driver.find_element(By.ID, "company").send_keys(USER["company"])
        driver.find_element(By.ID, "address1").send_keys(USER["address1"])
        driver.find_element(By.ID, "address2").send_keys(USER["address2"])
        Select(driver.find_element(By.ID, "country")).select_by_visible_text(USER["country"])
        driver.find_element(By.ID, "state").send_keys(USER["state"])
        driver.find_element(By.ID, "city").send_keys(USER["city"])
        driver.find_element(By.ID, "zipcode").send_keys(USER["zipcode"])
        driver.find_element(By.ID, "mobile_number").send_keys(USER["mobile"])

        # 13. Create Account
        safe_click(driver, (By.CSS_SELECTOR, "button[data-qa='create-account']"))

        # 14. Verify 'ACCOUNT CREATED!'
        heading = visible(driver, (By.CSS_SELECTOR, "h2[data-qa='account-created']"))
        assert heading.text.strip().upper() == "ACCOUNT CREATED!", f"Got: {heading.text!r}"
        print("'ACCOUNT CREATED!' is visible.")

        # 15. Continue
        safe_click(driver, (By.CSS_SELECTOR, "a[data-qa='continue-button']"))

        # 16. Verify 'Logged in as username'
        logged_in = visible(driver, (By.XPATH, "//a[contains(., 'Logged in as')]"))
        assert USER["name"] in logged_in.text, f"Got: {logged_in.text!r}"
        print(f"Verified: {logged_in.text.strip()}")

        # 17. Delete Account
        safe_click(driver, (By.CSS_SELECTOR, "a[href='/delete_account']"))

        # 18. Verify 'ACCOUNT DELETED!' and click Continue
        heading = visible(driver, (By.CSS_SELECTOR, "h2[data-qa='account-deleted']"))
        assert heading.text.strip().upper() == "ACCOUNT DELETED!", f"Got: {heading.text!r}"
        print("'ACCOUNT DELETED!' is visible.")
        safe_click(driver, (By.CSS_SELECTOR, "a[data-qa='continue-button']"))

        print("Register User test completed successfully.")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()