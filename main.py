from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import Options

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,800")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

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