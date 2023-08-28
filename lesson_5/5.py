from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def script5(driver):
    for x in range(1, 4):
        driver.get("http://uitestingplayground.com/classattr")
        driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
        alert = Alert(driver)
        alert_text = alert.text
        print(alert_text)
        assert alert_text == "Primary button pressed"
        alert.dismiss()
        driver.refresh()
    driver.quit()


driver1 = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
script5(driver1)

driver2 = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
script5(driver2)
