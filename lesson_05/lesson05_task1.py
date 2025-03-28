from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")


add_button = driver.find_element(By.CLASS_NAME, "btn-primary").click()


sleep(15)
