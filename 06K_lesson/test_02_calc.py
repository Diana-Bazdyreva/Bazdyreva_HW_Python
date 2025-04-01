import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calc(driver):

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay.send_keys(Keys.BACKSPACE)
    delay.send_keys("45")
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    sum = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert int(sum) == 15
