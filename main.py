from selenium import webdriver

# Start up
driver = webdriver.Chrome()
amazon_url = "http://www.amazon.com"
driver.get(amazon_url)

search_bar = driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
search = search_bar.send_keys('Java')
search_button = driver.find_element_by_xpath("//*[@id='nav-search-submit-button']")
search_button.click()
driver.quit()
