from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://45.79.43.178/source_carts/wordpress/wp-admin/")

user_input = driver.find_element_by_css_selector('#user_login')
user_input.send_keys('admin')

user_input = driver.find_element_by_css_selector('#user_pass')
user_input.send_keys('123456aA')

user_input = driver.find_element_by_css_selector('#wp-submit').click()

time.sleep(10)

username = driver.find_element_by_css_selector('#wp-admin-bar-site-name > a').text
print(username)