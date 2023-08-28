from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

from PIL import Image
from PIL import ImageChops  #pip install pillow - предварительно устанавливаем пакет для работы с картинками
import io

def script4(driver):
    for x in range(1, 4):
        driver.get("http://uitestingplayground.com/dynamicid")
        driver.find_element(By.CSS_SELECTOR, '.btn-primary').click() 
        driver.save_screenshot(f"image{x}.png") #делаем скрин
    driver.quit()

def compare (screen1, screen2):
    im1 = Image.open(screen1)
    im2 = Image.open(screen2)
    diff = ImageChops.difference(im1, im2)
    bbox = diff.getbbox()
    assert bbox is None, "Images do not match"

driver1 = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
script4(driver1)
compare("image1.png", "image2.png") #сравниваем скрины
compare("image2.png", "image3.png")
compare("image1.png", "image3.png")

driver2 = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
script4(driver2)
compare("image1.png", "image2.png") #сравниваем скрины
compare("image2.png", "image3.png")
compare("image1.png", "image3.png")
