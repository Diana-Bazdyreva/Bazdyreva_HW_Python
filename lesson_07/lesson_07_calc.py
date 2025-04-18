from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class Calculator:

    def __init__(self, driver):
        self.driver = driver

    def set_delay(self, delay_value):
        delay = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.send_keys(Keys.BACKSPACE)
        delay.send_keys(str(delay_value))

    def click_button(self, button):
        self.driver.find_element(
            By.XPATH, f"//span[text()='{button}']").click()

    def waiting(self, value):
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), str(value)))

    def get_screen_value(self):
        screen = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return screen.text.strip()
