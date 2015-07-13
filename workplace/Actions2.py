'''
Created on 10 Jul 2015

@author: Burn
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os

#from selenium.webdriver.support.ui import Select

profile = webdriver.FirefoxProfile(os.path.expanduser("C:/Users/Burn/AppData/Local/Mozilla/Firefox/Profiles/ropkk9mh.default"))
driver = webdriver.Firefox(profile)
driver.maximize_window()

driver.get("http://google.com")
search = driver.find_element_by_class_name("gsfi")
ActionChains(driver).move_to_element(search).context_click(search).perform()