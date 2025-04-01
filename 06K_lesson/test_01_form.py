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


def test_shopping_cart(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    first_name = driver.find_element(By.NAME, "first-name")
    first_name.send_keys("Иван")
    last_name = driver.find_element(By.NAME, "last-name")
    last_name.send_keys("Петров")
    address = driver.find_element(By.NAME, "address")
    address.send_keys("Ленина, 55-3")
    email = driver.find_element(By.NAME, "e-mail")
    email.send_keys("test@skypro.com")
    phone = driver.find_element(By.NAME, "phone")
    phone.send_keys("+7985899998787")
    city = driver.find_element(By.NAME, "city")
    city.send_keys("Москва")
    country = driver.find_element(By.NAME, "country")
    country.send_keys("Россия")
    job = driver.find_element(By.NAME, "job-position")
    job.send_keys("QA")
    company = driver.find_element(By.NAME, "company")
    company.send_keys("SkyPro")

    submit_but = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_but.click()

    def check_field_color(field_selector, expected_class):
        field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, field_selector))
        )
        act_class = field.get_attribute('class')
        assert act_class == expected_class, \
            f"Факт {expected_class}, план {act_class}"

    check_field_color("#first-name", "alert py-2 alert-success")
    check_field_color("#last-name", "alert py-2 alert-success")
    check_field_color("#address", "alert py-2 alert-success")
    check_field_color("#e-mail", "alert py-2 alert-success")
    check_field_color("#phone", "alert py-2 alert-success")
    check_field_color("#city", "alert py-2 alert-success")
    check_field_color("#country", "alert py-2 alert-success")
    check_field_color("#job-position", "alert py-2 alert-success")
    check_field_color("#company", "alert py-2 alert-success")

    check_field_color("#zip-code", "alert py-2 alert-danger")
