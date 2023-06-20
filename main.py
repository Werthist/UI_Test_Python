from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

URL = 'https://www.saucedemo.com/'

# ID: user-name, password, login-button

LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

driver.get(URL)

login_page_button = driver.find_element(By.ID, 'user-name')
login_page_button.click()

input_login= driver.find_element(By.ID, 'user-name')
input_password= driver.find_element(By.ID, 'password')

input_login.send_keys(LOGIN)
input_password.send_keys(PASSWORD)

click_page_button = driver.find_element(By.ID, 'login-button')
click_page_button.click()