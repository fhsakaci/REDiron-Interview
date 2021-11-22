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
#time.sleep(20)

#driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='Sign in or Create an Account']"))
#print(driver.page_source)
#time.sleep(1)

WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Sign in or Create an Account']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "loginForgotPassword"))).click()
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Password Assistance']")))

#test = driver.find_element_by_id("loginForgotPassword")
#test.click()

#driver.switch_to_default_content()

#print(driver.page_source)
#time.sleep(10)

#driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='Password Assistance']"))
#print(driver.page_source)
time.sleep(1)


#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.navigationbar__item a[data-link-name=' My Account'][href='/Sign In']"))).click()

#link = driver.find_element_by_xpath("//nav/div/ul/li[2]/a").click()
#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#time.sleep(100)
driver.close()
