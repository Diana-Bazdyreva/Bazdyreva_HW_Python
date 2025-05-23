from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, 'user-name')))
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.presence_of_element_located((By.ID, 'password')))
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'btn_action')))
        login_button.click()


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self):
        backpack_add_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')))
        backpack_add_button.click()

    def add_bolt_tshirt_to_cart(self):
        tshirt_add_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')))
        tshirt_add_button.click()

    def add_onesie_to_cart(self):
        onesie_add_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')))
        onesie_add_button.click()

    def go_to_cart(self):
        cart_icon = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#shopping_cart_container a')))
        cart_icon.click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def proceed_to_checkout(self):
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkout')))
        checkout_button.click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form_data(self, first_name, last_name, zip_code):
        first_name_field = self.wait.until(
            EC.presence_of_element_located((By.ID, 'first-name')))
        first_name_field.send_keys(first_name)

        last_name_field = self.wait.until(
            EC.presence_of_element_located((By.ID, 'last-name')))
        last_name_field.send_keys(last_name)

        zip_code_field = self.wait.until(
            EC.presence_of_element_located((By.ID, 'postal-code')))
        zip_code_field.send_keys(zip_code)

    def submit_order(self):
        continue_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#continue')))
        continue_button.click()


class CheckoutCompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_total_amount(self):
        total_amount = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'summary_total_label'))).text
        return total_amount.strip('Total: ')
