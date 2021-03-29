from time import sleep
import unittest
from main import TestSelenium
from selenium import webdriver


class SeleniumTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Test starts')
        cls.driver = webdriver.Chrome()
        cls.amazon_url = "http://www.amazon.com"
        cls.url_google = "http://www.google.com"
        cls.url_video = "https://videojs.com/"

    def tearDownClass(cls):
        print("Test ends")

    def amazon_search(self, *search_items):
        self.amazon = TestSelenium(self.driver, self.amazon_url)
        print(self.amazon)
        if len(search_items) > 1:
            self.amazon.keyboard_locator(*search_items)
        elif len(search_items) == 1:
            self.amazon.mouse_operation(*search_items)
        else:
            pass
        self.amazon.tear_down()

    def google_search(self):
        google = TestSelenium(self.driver, self.url_google)
        print(google)

        google.mutiple_locators("selenium book")
        google.tear_down()

    def video_play(self):
        play_video = TestSelenium(self.driver, self.url_video)
        print(play_video)
        play_video.video_play()
        sleep(20)
        play_video.tear_down()

    def scroll_up_down(self):
        scroll_test = TestSelenium(self.driver, self.amazon_url)
        print(scroll_test)
        scroll_test.scroll_up_down_amazon(self.amazon_url)
        sleep(10)
        scroll_test.tear_down()

    def test_search_amazon(self):
        print('Test amazon')
        self.amazon_search("java")

    def test_google(self):
        print('Test google')
        self.google_search()

    def test_video(self):
        print('Test video plays')
        self.video_play()

    def test_scrolling(self):
        print('Test scroll up and down on page')
        self.scroll_up_down()


# This is necessary
if __name__ == '__main__':
    unittest.main()
