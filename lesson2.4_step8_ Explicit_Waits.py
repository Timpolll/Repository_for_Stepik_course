from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
button = browser.find_element(By.TAG_NAME, "button")
button.click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

input = browser.find_element(By.CSS_SELECTOR, "input[type='text']")
input.send_keys(y)

time.sleep(1)

button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
button.click()

time.sleep(5)