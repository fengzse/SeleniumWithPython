from time import sleep

from main import TestSelenium
from selenium import webdriver

driver = webdriver.Chrome()


def amazon_search(choice):
    amazon_url = "http://www.amazon.com"
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
    url = "http://www.google.com"
    google = TestSelenium(driver, url)
    print(google)

    google.mutiple_locators("selenium book")
    google.tear_down()


def video_play():
    url = "https://videojs.com/"
    play_video = TestSelenium(driver, url)
    print(play_video)
    play_video.video_play()
    sleep(20)
    play_video.tear_down()


video_play()
