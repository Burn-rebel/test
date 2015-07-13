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

driver.get('http://tizag.com/javascriptT/javascriptalert.php')
driver.find_element_by_xpath("//div[@class='display']/form/input").click()
print(driver.switch_to_alert().text)

driver.switch_to_alert().accept()

driver.get('http://paytm.com')
count=driver.find_elements_by_tag_name('a')
print len(count)

footercount=driver.find_element_by_xpath(".//*[@id='footerlink']").find_elements_by_tag_name("a")
print len(footercount)

for op in footercount:
    op.click()
    
    