"""Parameterization and fixtures: login test for all saucedemo.com users

Run with:  pytest -v test_saucedemo_login.py
Headless:  HEADLESS=1 pytest -v test_saucedemo_login.py
"""
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://www.saucedemo.com/"
PASSWORD = "secret_sauce"
PRODUCT = "Sauce Labs Backpack"

# (username, should_login_successfully)
USERS = [
    ("standard_user", True),
    ("locked_out_user", False),
    ("problem_user", True),
    ("performance_glitch_user", True),
    ("error_user", True),
    ("visual_user", True),
]


@pytest.fixture
def driver():
    options = Options()
    if os.getenv("HEADLESS"):
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    # Disable Chrome's password-leak / save-password popups that can appear after login
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()


def login(driver, username, password=PASSWORD):
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


@pytest.mark.parametrize("username, should_login", USERS, ids=[u for u, _ in USERS])
def test_login(driver, username, should_login):
    login(driver, username)
    wait = WebDriverWait(driver, 15)  # performance_glitch_user is intentionally slow

    if should_login:
        wait.until(EC.url_contains("inventory.html"))
        title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title")))
        assert title.text == "Products"

        names = [e.text for e in driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
        assert PRODUCT in names, f"{PRODUCT!r} missing for {username}. Found: {names}"
    else:
        error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
        assert "locked out" in error.text.lower()
        assert "inventory.html" not in driver.current_url