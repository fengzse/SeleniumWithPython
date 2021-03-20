from main import TestSelenium
from selenium import webdriver

driver = webdriver.Chrome()


def amazon_search():
    amazon_url = "http://www.amazon.com"
    amazon = TestSelenium(driver, amazon_url)
    print(amazon)
    amazon.keyboard_locator('selenium book', 'java', 'python')
    amazon.mouse_operation('Java')
    amazon.tear_down()


def google_search():
    url = "http://www.google.com"
    google = TestSelenium(driver, url)
    print(google)

    google.mutiple_locators("selenium book")
    google.tear_down()


google_search()
