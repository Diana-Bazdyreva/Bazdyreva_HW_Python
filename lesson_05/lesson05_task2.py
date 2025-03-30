from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")


add_button = driver.find_element(By.CLASS_NAME, "btn-primary").click()
