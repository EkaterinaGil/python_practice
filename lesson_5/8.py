from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

def script8(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    username_field = driver.find_element(By.CSS_SELECTOR, '#username')
    password_field = driver.find_element(By.CSS_SELECTOR, '#password')
    login_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    username_field.send_keys("tomsmith")
    password_field.send_keys("SuperSecretPassword!")
    login_button.click()
    driver.quit()

driver1 = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
script8(driver1)

driver2 = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
script8(driver2)
