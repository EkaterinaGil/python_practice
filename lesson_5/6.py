from selenium import webdriver
from time import sleep

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

def script6(driver):
    driver.get("https://the-internet.herokuapp.com/entry_ad")
    sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element(By.CSS_SELECTOR, 'div.modal-footer p').click()
    driver.quit()

driver1 = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
script6(driver1)

driver2 = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
script6(driver2)
