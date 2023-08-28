from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

def script3(driver):
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    for x in range(1, 6):
        driver.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]').click()

    elems = driver.find_elements(By.CSS_SELECTOR, '#elements button')

    print(len(elems))
    driver.quit() 

driver1 = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

script3(driver1)

driver2 = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

script3(driver2)