from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


driver = webdriver.Firefox()
driver.get("https://www.barnesandnoble.com/h/books/browse")
print(driver.title)

select_box = driver.find_element_by_id("navbarDropdown") 
select_box.click()
time.sleep(1)
driver.find_element_by_partial_link_text("Sign In").click()
time.sleep(10)

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='Sign in or Create an Account']"))

time.sleep(10)

element = driver.find_element_by_id("loginForgotPassword") 
driver.execute_script("arguments[0].click();", element)
time.sleep(5)

driver.switch_to_default_content()
time.sleep(5)
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='Password Assistance']"))
inputElement = driver.find_element_by_id("email")
inputElement.send_keys('furkan.sakaci@gmail.com')
driver.find_element_by_id('forgotPasswordForm').submit()

time.sleep(4)
error = driver.find_element_by_id('passwordAssistantErr')
print(error.text)

driver.close()
