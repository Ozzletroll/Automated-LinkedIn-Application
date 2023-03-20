import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# LinkedIn Login details
username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]

# Selenium driver setup
service = Service("C:/Program Files (x86)/Google/Chrome/chromedriver.exe")
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

# LinkedIn Login
driver.get("https://www.linkedin.com/login?emailAddress=&fromSignIn=&fromSignIn=true&session_redirect=https%3A%2F"
           "%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3FcurrentJobId%3D3532055392%26f_LF%3Df_AL%26geoId%3D102257491"
           "%26keywords%3Dpython%2520developer%26location%3DLondon%252C%2520England%252C%2520United%2520Kingdom&trk"
           "=public_jobs_nav-header-signin")
email_field = driver.find_element(By.CSS_SELECTOR, "#username")
email_field.click()
email_field.send_keys(username)
password_field = driver.find_element(By.CSS_SELECTOR, "#password")
password_field.click()
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)
time.sleep(5)

