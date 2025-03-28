from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")


input_f = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_f.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()

print(button.text)


driver.quit()
