from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.implicitly_wait(20)

driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()
element = driver.find_element(By.CSS_SELECTOR, "#content>.bg-success")
text_content = element.text
driver.quit()

print(text_content)
