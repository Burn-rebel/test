'''
Created on 10 Jul 2015

@author: Burn
'''
from selenium import webdriver

import os

#from selenium.webdriver.support.ui import Select

profile = webdriver.FirefoxProfile(os.path.expanduser("C:/Users/Burn/AppData/Local/Mozilla/Firefox/Profiles/ropkk9mh.default"))
driver = webdriver.Firefox(profile)
driver.maximize_window()
driver.get("https://accounts.google.com/signup")
print (driver.title)
parent = driver.current_window_handle
driver.find_element_by_xpath(".//*[@id='wrapper']/div[2]/div/div[1]/p/a").click()

wh = driver.window_handles[-1]
driver.switch_to_window(wh)
print (driver.title)
driver.switch_to_window(parent)
print (driver.title)
c = driver.get_cookies()
print len(c)
print c