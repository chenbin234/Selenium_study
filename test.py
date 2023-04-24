from selenium import webdriver
import time

drivers = webdriver.Chrome()
drivers.get('https://www.baidu.com')

# Find the search bar and enter text
search_box = drivers.find_element('id','kw')
search_box.send_keys("dogs pictures")

# Find the search button and click it
search_button = drivers.find_element('id','su')
search_button.click()


time.sleep(20)
drivers.quit()
