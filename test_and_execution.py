from time import sleep
import unittest
from main import TestSelenium
from selenium import webdriver


class SeleniumTest(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        print('Test starts')
        cls.driver = webdriver.Chrome()
        cls.amazon_url = "http://www.amazon.com"
        cls.url_google = "http://www.google.com"
        cls.url_video = "https://videojs.com/"

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()
        print("Test ends")

    def amazon_search(self, *search_items, key_words=''):
        self.amazon = TestSelenium(self.driver, self.amazon_url)
        print(self.amazon)
        if len(search_items) > 1:
            self.amazon.keyboard_locator(*search_items)
        elif len(search_items) == 1:
            self.amazon.mouse_operation(search_items, key_words)
        else:
            pass

    def google_search(self):
        google = TestSelenium(self.driver, self.url_google)
        print(google)

        google.mutiple_locators("selenium book")

    def video_play(self):
        play_video = TestSelenium(self.driver, self.url_video)
        print(play_video)
        play_video.video_play()
        sleep(20)

    def scroll_up_down(self):
        scroll_test = TestSelenium(self.driver, self.amazon_url)
        print(scroll_test)
        scroll_test.scroll_up_down_amazon(self.amazon_url)
        sleep(10)

    def test_search_amazon(self):
        print('Test amazon')
        self.amazon_search("java", key_words="The Complete Reference")

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
    test_suite = unittest.TestSuite()
    test_suite.addTest(SeleniumTest('test_search_amazon'))

    runner = unittest.TextTestRunner()
    runner.run(test_suite)
