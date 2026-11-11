"""Task 1 - Web automation with Selenium: login + product verification on saucedemo.com"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
PRODUCT = "Sauce Labs Backpack"


def main():
    driver = webdriver.Chrome()  # Selenium 4.6+ downloads the driver automatically
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Login
        driver.get(URL)
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "login-button").click()

        # Verify login succeeded: URL and page title element
        wait.until(EC.url_contains("inventory.html"))
        title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title")))
        assert title.text == "Products", f"Unexpected page title: {title.text!r}"
        print("Login successful - Products page is displayed.")

        # 2. Verify the specific product
        names = [e.text for e in driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
        assert PRODUCT in names, f"{PRODUCT!r} not found. Products on page: {names}"

        product_el = driver.find_element(
            By.XPATH, f"//div[contains(@class,'inventory_item_name')][normalize-space()='{PRODUCT}']"
        )
        assert product_el.is_displayed(), f"{PRODUCT!r} is present but not displayed"
        print(f"Product verified: {PRODUCT}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()