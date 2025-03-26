from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")


search_str = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
search_str.send_keys("Sky")


sleep(3)


search_str.clear()
search_str.send_keys("Pro")


sleep(5)


driver.quit()


sleep(5)
