import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
time.sleep(30)

browser.get('http://www.google.com')
WebDriverWait(driver, 10)
search = browser.find_element_by_name('q')
search.send_keys("google search through python")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(50) # sleep for 5 seconds so you can see the results
browser.quit()
