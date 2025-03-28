from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")


blue_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
blue_button.click()


driver.implicitly_wait(18)


green_element = driver.find_element(By.CSS_SELECTOR, "p.bg-success")
print(green_element.text)


driver.quit()
