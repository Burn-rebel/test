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

driver.get("http://jqueryui.com/tooltip")
frm = driver.find_element_by_class_name("demo-frame")
driver.switch_to_frame(frm)
driver.find_element_by_xpath(".//*[@id='age']").send_keys("24")
driver.switch_to_default_content()
driver.find_element_by_xpath(".//*[@id='sidebar']/aside[1]/ul/li[1]/a").click()

