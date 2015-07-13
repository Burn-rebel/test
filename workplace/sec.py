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

driver.get('http://airindia.in')
driver.find_element_by_xpath("//*[@class='iradio checked']/input").click()

radio = driver.find_element_by_xpath("//*[@class='iradio checked']/ins")
driver.implicitly_wait(5)
if radio.is_selected():
    print 'Yes is selected'
else:
    print 'No is selected'

