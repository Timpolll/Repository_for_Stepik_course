import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button(browser):
    browser.get(link)
    time.sleep(2)
    try:
        # Try to find the button and assert its existence
        button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert button is not None, "Add to basket button not found"
    except NoSuchElementException:
        # If the element is not found, raise the assertion with a custom message
        assert False, "Add to basket button not found due to NoSuchElementException"