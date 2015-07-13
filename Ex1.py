'''
Created on 9 july 2015

@author: burn
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://airindia.in")
driver.implicitly_wait(100)
driver.find_element_by_id("from").send_keys('ban')

driver.implicitly_wait(4)

driver.find_element_by_partial_link_text("Colombo").click()
dropdown = Select(driver.find_element_by_xpath(".//*[@id='_classType1']"))
dropdown.select_by_value('Business')
print(driver.find_element_by_xpath(".//*[@id='_classType1']").text)


