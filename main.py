from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://localhost:8002/wordpress/wp-admin')

admin = driver.find_element(By.XPATH,'.//*[@id="user_login"]')
admin.send_keys('user')

password = driver.find_element(By.XPATH,'.//*[@id="user_pass"]')
password.send_keys('#CatalinCaldararu#')

button = driver.find_element(By.XPATH,'.//*[@id="wp-submit"]')
time.sleep(2)
button.click()

time.sleep(2)
driver.get('http://localhost:8002/wordpress/wp-admin/post-new.php')

title = driver.find_element(By.XPATH,'.//*[@id="post-title-0"]') 
title.send_keys('This is a test. #3')
sleep(2)

driver.find_element_by_xpath("//button[text()='Publish']").click()
sleep(2)

driver.find_element_by_css_selector('button.components-button.editor-post-publish-button.editor-post-publish-button__button.is-primary').click()
sleep(2)
