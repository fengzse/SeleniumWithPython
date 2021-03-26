from time import sleep

from main import TestSelenium
from selenium import webdriver

driver = webdriver.Chrome()
amazon_url = "http://www.amazon.com"
url_google = "http://www.google.com"
url_video = "https://videojs.com/"


def amazon_search(choice):
    amazon = TestSelenium(driver, amazon_url)
    print(amazon)
    if choice == 1:
        amazon.keyboard_locator('selenium book', 'java', 'python')
    elif choice == 2:
        amazon.mouse_operation('Java')
    else:
        pass
    amazon.tear_down()


def google_search():
    google = TestSelenium(driver, url_google)
    print(google)

    google.mutiple_locators("selenium book")
    google.tear_down()


def video_play():
    play_video = TestSelenium(driver, url_video)
    print(play_video)
    play_video.video_play()
    sleep(20)
    play_video.tear_down()


def scroll_up_down():
    scroll_test = TestSelenium(driver,amazon_url)
    print(scroll_test)
    scroll_test.scroll_up_down_amazon(amazon_url)
    sleep(10)
    scroll_test.tear_down()


scroll_up_down()
