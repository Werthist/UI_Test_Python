from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))

from selenium.webdriver.common.by import By

# !!INPUT YOUR VALUES!! I am too lazy to do input box:
#------------------------------------
URL = 'https://www.saucedemo.com/'
#------------------------------------
login = 'standard_user'
#------------------------------------
password = 'secret_sauce'
#------------------------------------
# ID: user-name, password, login-button (site id's)

def open_browser(driver, URL):
    driver.get(URL)

def get_element_by_id(driver, locator):
    return driver.find_element(By.ID, locator)

def element_click(driver, locator):
    element = get_element_by_id(driver,locator)
    element.click()

def element_sendkey(driver, locator, text):
    element = get_element_by_id(driver,locator)
    element.send_keys(text)

def auth(driver, login, password):
    element_sendkey(driver, 'user-name', login)
    element_sendkey(driver, 'password', password)
    element_click(driver, 'login-button')
    
#1-----Get your site in browser------
open_browser(driver, URL)
#2-----Authenticator------
auth(driver, login, password)

driver.quit()