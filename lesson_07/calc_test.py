import pytest
from selenium import webdriver
from lesson_07_calc import Calculator


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calc(browser):
    calculator = Calculator(browser)
    calculator.set_delay(2)
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")
    calculator.waiting("15")
    actual_sum = calculator.get_screen_value()

    assert int(actual_sum) == 15
