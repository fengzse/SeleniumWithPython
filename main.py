from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains, TouchActions
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestSelenium:
    def __init__(self, driver=None, url_insert=None):
        # SetUp
        self.driver = driver
        self.url = url_insert
        self.driver.get(self.url)

    def __repr__(self):
        return "Now accessing to %s" % self.url

    # def set_windows(self):
    # self.driver.set_window_size(480,800)
    # self.driver.maximize_window()

    def keyboard_locator(self, *search_items):
        """
        Can not assign element-locator to vars and reuse them in the loop, have to re-locate in the loop
        search_bar = self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
        search_button = self.driver.find_element_by_xpath("//*[@id='nav-search-submit-button']")
        """
        # Element locator
        for i in search_items:
            search_bar = self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
            search_button = self.driver.find_element_by_xpath("//*[@id='nav-search-submit-button']")
            search_bar.send_keys(i)
            '''
            used to code 
                search=self.search_bar.send_keys(i)
                search.submit() -->  couldn't work
            correct way
                search_bar.submit() --> works
            '''
            search_button.click()
            print('Found %s items on Amazon' % i)
            self.driver.back()
            # search_bar.clear()

    def mouse_operation(self, search_item, key_words):
        search_bar = self.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
        search_bar.send_keys(search_item)
        search_bar.submit()

        if key_words!='':
            try:
                WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, key_words)))
            except TimeoutError:
                print('Time out')
                self.driver.quit()

            element_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, key_words)
            ActionChains(self.driver).move_to_element(element_link).perform()
            WebDriverWait(self.driver, 5)
            ActionChains(self.driver).click().perform()
        else:
            self.driver.quit()

        try:
            WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "// *[@id = 'rentButton']")))
        except TimeoutError:
            print('Time out')
            self.driver.quit()

        element_button = self.driver.find_element(By.XPATH, "// *[@id = 'rentButton']")
        ActionChains(self.driver).move_to_element(element_button).perform()
        ActionChains(self.driver).click().perform()
        try:
            WebDriverWait(self.driver, 5).until(
                ec.text_to_be_present_in_element((By.XPATH, "//*[@id='huc-v2-order-row-confirm-text']/h1"),
                                                 "Added to Cart"))
            print('Ready to buy')
        except NoSuchElementException:
            print('Time out')
            self.driver.quit()

    def mutiple_locators(self, search_item):
        search_bar = self.driver.find_element(By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > "
                                                               "form > div:nth-child(1) > div.A8SBwf > "
                                                               "div.RNNXgb > div > div.a4bIc > input")
        search_bar.send_keys(search_item)
        search_bar.submit()

        search_results = self.driver.find_elements(By.CLASS_NAME, "FozYP")
        print(len(search_results))
        for i in search_results:
            print(i.text)

    def video_play(self):
        video = self.driver.find_element(By.XPATH, "//*[@id='vjs_video_3_html5_api']")

        video_src = self.driver.execute_script("return arguments[0].currentSrc;", video)

        try:
            print("Strat playing" + video_src)
            self.driver.execute_script("arguments[0].play()", video)
        except:
            print("Video not found")
        else:
            print("Video can be played")

    def scroll_up_down_amazon(self, url):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.get(url)
        self.driver.maximize_window()

        search_bar = self.driver.find_element(By.XPATH, "//*[@id='twotabsearchtextbox']")
        search_bar.send_keys("selenium book")
        search_bar.submit()

        start = self.driver.find_element(By.XPATH, "//*[@id='search']/span/div/span/h1/div/div[1]/div/div")
        action = TouchActions(self.driver)
        try:
            action.tap(start)
            action.scroll_from_element(start, 0, 500).perform()
        except:
            print("Fail to scroll")
        else:
            print("Succeed")


