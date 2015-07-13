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

driver.get("http://spicejet.com")
ab = driver.find_element_by_xpath(".//*[@id='smoothmenu1']/ul/li[4]/a")
ActionChains(driver).move_to_element(ab).perform()
driver.implicitly_wait(5)
bd = driver.find_element_by_xpath(".//*[@id='smoothmenu1']/ul/li[4]/ul/li[2]/a")
ActionChains(driver).move_to_element(bd).perform()
driver.implicitly_wait(5)
dc = driver.find_element_by_xpath(".//*[@id='smoothmenu1']/ul/li[4]/ul/li[2]/ul/li[1]/a")
ActionChains(driver).move_to_element(dc).perform()
driver.implicitly_wait(5)
ce = driver.find_element_by_xpath(".//*[@id='smoothmenu1']/ul/li[4]/ul/li[2]/ul/li[1]/ul/li[1]/a")
ActionChains(driver).move_to_element(ce).click(ce).perform()
