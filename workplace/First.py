'''
Created on 10 Jul 2015

@author: Burn
'''
from selenium import webdriver

import os

from selenium.webdriver.support.ui import Select

profile = webdriver.FirefoxProfile(os.path.expanduser("C:/Users/Burn/AppData/Local/Mozilla/Firefox/Profiles/ropkk9mh.default"))
driver = webdriver.Firefox(profile)
driver.maximize_window()

driver.get('http://airindia.in')

driver.find_element_by_id("from").send_keys('ban')
driver.implicitly_wait(10)
driver.find_element_by_partial_link_text('Colombo').click()

driver.find_element_by_id('to').send_keys('del')
driver.implicitly_wait(10)
driver.find_element_by_partial_link_text('Delhi').click()

dropdown = Select(driver.find_element_by_id('_classType1'))
dropdown.select_by_visible_text('Executive/Economy')
print 'This value was selected in dropdownbox'
print(driver.find_element_by_xpath("//div[@id='divclasstype1']/span/span").text)

radio_d = driver.find_element_by_css_selector(".iCheck-helper")

driver.implicitly_wait(10)

if radio_d.is_selected():
    print 'Yes is selected'
else: 
    print 'No is selected'