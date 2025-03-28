from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")


username = driver.find_element(By.ID, 'username')
username.send_keys("tomsmith")


password = driver.find_element(By.ID, 'password')
password.send_keys("SuperSecretPassword!")


button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


green_line = driver.find_element(By.ID, 'flash')
print(green_line.text)


driver.quit()


sleep(5)
