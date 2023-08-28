from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

def script7(driver):
    driver.get("https://the-internet.herokuapp.com/inputs")
    input_field = driver.find_element(By.CSS_SELECTOR, 'div input')
    input_field.send_keys("1000")
    input_field.clear()
    input_field.send_keys("999")
    driver.quit()

driver1 = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
script7(driver1)

driver2 = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
script7(driver2)
