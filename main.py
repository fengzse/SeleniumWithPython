from time import sleep

from selenium import webdriver
from selenium.webdriver.support import wait


class TestSelenium:
    def __init__(self, url_insert):
        # Start up
        self.driver = webdriver.Chrome()
        self.url = url_insert
        self.driver.get(self.url)
        self.search_bar = None
        self.search_button = None
        self.search = None

    def __repr__(self):
        return 'Now accessing to %s' % self.url

    def func(self, *search_items):
        """
        Can not assign element-locating to vars and reuse them in the loop, have to re-locate in the loop
        self.search_bar = self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
        self.search_button = self.driver.find_element_by_xpath("//*[@id='nav-search-submit-button']")
        """
        # Element locating
        for i in search_items:
            self.search_bar = self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
            self.search_button = self.driver.find_element_by_xpath("//*[@id='nav-search-submit-button']")
            self.search_bar.send_keys(i)
            '''
            used to code 
                self.search=self.search_bar.send_keys(i)
                self.search.submit() -->  couldn't work
            correct way
                self.search_bar.submit() --> works
            '''
            self.search_button.click()
            print('Found %s items on Amazon' % i)
            self.driver.back()
            # self.search_bar.clear()

    # def set_windows(self):
    # self.driver.set_window_size(480,800)
    # self.driver.maximize_window()

    # break
    def break_connection(self):
        self.driver.quit()
