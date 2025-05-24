import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from page_shop_allure import MainPage, CartPage
from page_shop_allure import CheckoutPage, CheckoutCompletePage, LoginPage
import allure


@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.title("Покупка в магазине одежды")
@allure.description("Тест проверяет покупку трех позиций в магазине одежды")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(browser):
    WebDriverWait(browser, 10)

    browser.get("https://www.saucedemo.com/")

    with allure.step("Открытие главное страницы магазина"):
        login_page = LoginPage(browser)
    with allure.step("Ввод логина"):
        login_page.enter_username("standard_user")
    with allure.step("Ввод пароля"):
        login_page.enter_password("secret_sauce")
    with allure.step("Нажатие кнопки входа"):
        login_page.click_login_button()

    with allure.step("Открытие страницы каталога магазина"):
        inventory_page = MainPage(browser)
    with allure.step("Добавление рюкзака в корзину"):
        inventory_page.add_backpack_to_cart()
    with allure.step("Добавление футболки в корзину"):
        inventory_page.add_bolt_tshirt_to_cart()
    with allure.step("Добавление боди в корзину"):
        inventory_page.add_onesie_to_cart()
    with allure.step("Переход в корзину"):
        inventory_page.go_to_cart()

    cart_page = CartPage(browser)
    with allure.step("Переход к оплате"):
        cart_page.proceed_to_checkout()

    checkout_step_one_page = CheckoutPage(browser)
    with allure.step("Заполнение контактных данных"):
        checkout_step_one_page.fill_form_data("Diana", "Bazdyreva", "400002")
    with allure.step("Подтверждение покупки"):
        checkout_step_one_page.submit_order()

    checkout_complete_page = CheckoutCompletePage(browser)
    with allure.step("Получение финальной суммы"):
        actual_total = checkout_complete_page.get_total_amount()
        expected_total = "$58.29"
    with allure.step("Проверка финальной суммы"):
        assert actual_total == expected_total, (f"Ожидалось {
            expected_total}, получено {actual_total}"
        )
