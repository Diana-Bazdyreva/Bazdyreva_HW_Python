import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_shop(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    username_input = wait.until(
        EC.presence_of_element_located((By.ID, "user-name")))
    username_input.send_keys("standard_user")

    password_input = wait.until(
        EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys("secret_sauce")

    login_button = driver.find_element(By.CLASS_NAME, "btn_action")
    login_button.click()

    add_backpack = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")))
    add_backpack.click()

    add_tshirt = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")))
    add_tshirt.click()

    add_onesie = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")))
    add_onesie.click()

    cart_icon = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#shopping_cart_container")))
    cart_icon.click()

    checkout_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#checkout")))
    checkout_button.click()

    first_name_field = wait.until(EC.element_to_be_clickable(
        (By.ID, "first-name"))) 
    first_name_field.send_keys("Diana")
    last_name_field = wait.until(EC.element_to_be_clickable(
        (By.ID, "last-name")))
    last_name_field.send_keys("Bazdyreva")

    postal_code_field = wait.until(EC.element_to_be_clickable(
        (By.ID, "postal-code")))
    postal_code_field.send_keys("400002")

    continue_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#continue")))
    continue_button.click()

    total_amount = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "summary_total_label"))).text
    expected_total = "Total: $58.29"
    assert total_amount == expected_total, \
        f"План {expected_total}, факт {total_amount}"
