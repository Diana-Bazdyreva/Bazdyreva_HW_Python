import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from lesson_07_shop import LoginPage
from lesson_07_shop import MainPage
from lesson_07_shop import CartPage
from lesson_07_shop import CheckoutPage
from lesson_07_shop import CheckoutCompletePage


@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_shop(browser):
    WebDriverWait(browser, 10)

    browser.get("https://www.saucedemo.com/")

    login_page = LoginPage(browser)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()

    inventory_page = MainPage(browser)
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bolt_tshirt_to_cart()
    inventory_page.add_onesie_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.proceed_to_checkout()

    checkout_step_one_page = CheckoutPage(browser)
    checkout_step_one_page.fill_form_data("Diana", "Bazdyreva", "400002")
    checkout_step_one_page.submit_order()

    checkout_complete_page = CheckoutCompletePage(browser)
    actual_total = checkout_complete_page.get_total_amount()
    expected_total = "$58.29"
    assert actual_total == expected_total, f"Ожидалось {
        expected_total}, получено {actual_total}"
