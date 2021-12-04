from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip as pc
import os

directory = os.getcwd()

def articleUpload(driver, route):
    for r, _, f in os.walk(r'articles'):
        for _f in f:
            apath = os.path.join(r, _f)
            _, ext = os.path.splitext(apath)
            if ext == '.txt':
                try:
                    driver.get(route)
                    with open(apath) as text:
                        words = text.read()
                        title = driver.find_element(By.XPATH, './/*[@id="post-title-0"]')
                        pc.copy(words)
                        title.send_keys(Keys.CONTROL, 'v')

                        driver.find_element_by_xpath("//button[text()='Publish']").click()
                        sleep(2)
                        driver.find_element_by_css_selector('button.components-button.editor-post-publish-button.editor-post-publish-button__button.is-primary').click()
                        sleep(2)
                except Exception as e:
                    print(f'Error while processing {apath} -> {e}')

#Change your credentials accordingly
username = "user"
pas = "#CatalinCaldararu#"
route = "http://localhost:8002/wordpress/wp-admin/post-new.php"

#Login to Wordpress
driver = webdriver.Chrome()
driver.get('http://localhost:8002/wordpress/wp-admin')

admin = driver.find_element(By.XPATH,'.//*[@id="user_login"]')
admin.send_keys(username)

password = driver.find_element(By.XPATH,'.//*[@id="user_pass"]')
password.send_keys(pas)

button = driver.find_element(By.XPATH,'.//*[@id="wp-submit"]')
time.sleep(2)
button.click()
time.sleep(2)

#Start uploading articles from a directory with subdirectories
articleUpload(driver, route)


