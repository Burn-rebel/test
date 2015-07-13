'''
Created on 23 july 2015

@author: burn
'''
print 'hello alex'

from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://www.facebook.com')

print 'welcome to ' + driver.title + ' page'

print 'So you have entered start page'

driver.forward()

print 'This message is shown after forward method'

#input id="email" class="inputtext" type="text" tabindex="1" value="" name="email"

driver.find_element_by_xpath("//input[@name='lastname']").send_keys('Correct')
print 'I understand lesson and write correct xpath path'
print(driver.find_element_by_id("u_0_s").text)


#print 'Error message is shown'

#driver.close()
#driver.quit()
