'''
Created on 23 july 2015

@author: burn
'''
print 'hello alex'

from selenium import webdriver

driver = webdriver.Firefox()

driver.get('http://192.168.0.72/hims')

print 'welcome to ' + driver.title + ' page'

print 'So you have entered start page'

driver.forward()

print 'This message is shown after forward method'

driver.find_element_by_name('Item2.JobCode').send_keys('JobCodeKey')
driver.find_element_by_xpath(".//*[@id='logingRight']/form/input[1]").click()
print 'Click on submit button'

driver.find_element_by_xpath(".//*[@id='logingRight']/div/div[1]/span").is_displayed()
print 'Error message is shown'
#driver.close()
#driver.quit()
