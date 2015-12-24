import os

import unittest

from appium import webdriver

from selenium.common.exceptions import NoSuchElementException


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    countFirst = 0
    countSecond = 0
    _error = 0
    _none = 0
    def setUp(self):
        _myapp = 'com.paycasso.demo'
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            '../../../workspace/Appium/Android_app/app-debug.apk'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(25)
        
        login = self.driver.find_element_by_name("Login")
        login.click()
        login.send_keys('sa')
        
        self.driver.back()
        
        password = self.driver.find_element_by_id(_myapp + ':id/editPassword')
        password.click()
        password.send_keys('verify10')

        self.driver.back()

        Authorize = self.driver.find_element_by_name("Authorize")
        Authorize.click()
        
        

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_goto_products(self):
        count = 23
        count_9 = 2
        for attempt in range(8, 20):            
            _myapp = 'com.paycasso.demo'
            try:
                btn = self.driver.find_element_by_id(_myapp + ':id/buttonDocuSure')
                btn.click()
        
                start = self.driver.find_element_by_name('Start registration')
                start.click()
        
        
                self.driver.find_element_by_id(_myapp + ':id/btn_saved_image').click() #locating saved images button
        
    # Finding & selecting element in gallery
                s = self.driver.find_elements_by_class_name("android.view.View")
                print ("Attempt number: " + str(attempt))
                print ('-'*30)
                if attempt >= 9:
                    self.driver.swipe(958, 922, 958, 350)
                    k = s[count_9]
                    k.click()
                    count_9 +=3
                else:
                    k = s[count]
                    k.click()
                    count+=3
        
        # Check which button is displayed
            
                try: 
                    if self.driver.find_element_by_id(_myapp + ":id/buttonSkip").is_displayed():
                        SimpleAndroidTests.countFirst+=1
                        self.driver.find_element_by_id(_myapp + ":id/buttonSkip").click()
                        log = open("../../../workspace/Appium/Android_app/MRZ_logs_true.txt", 'r+')
                        log.write("Number of first read attempts " + str(SimpleAndroidTests.countFirst))
                        print "First attempt passed"
                        print ("Number of passed transactions: " + str(SimpleAndroidTests.countFirst))
                except NoSuchElementException:
                    print ("No Skip Button")
                    print ("First attempt failed")
                    try:
                        if self.driver.find_element_by_id(_myapp + ":id/buttonReCapture").is_displayed():
                            
                            Capture_id = self.driver.find_element_by_id(_myapp + ":id/buttonReCapture")
                            Capture_id.click()
                
        # Finding & selecting element in gallery
                            s = self.driver.find_elements_by_class_name("android.view.View")
                            if attempt >= 9:
                                self.driver.swipe(958, 922, 958, 3530)
                                k = s[count_9]
                                k.click()
                                
                            else:
                                k = s[count]
                                k.click()
        
                            try:
                                if self.driver.find_element_by_id(_myapp + ":id/buttonSkip").is_displayed():
                                    SimpleAndroidTests.countSecond+=1
                                    log = open("../../../workspace/Appium/Android_app/MRZ_logs_false.txt", 'r+')
                                    log.write("Number of second read attempts " + str(SimpleAndroidTests.countSecond))
                                    self.driver.find_element_by_id(_myapp + ":id/buttonSkip").click()
                                    print "Second attempt passed"
                                    print ("Number of second passed transactions: " + str(SimpleAndroidTests.countSecond))
                            except NoSuchElementException:
                                SimpleAndroidTests._none +=1
                                log = open("../../../workspace/Appium/Android_app/MRZ_logs_None.txt", 'r+')
                                log.write("Number of attempts with errors: " + str(SimpleAndroidTests._none))
                                print "Second attempt failed"
                                print ("Number of failed attempts: " + str(SimpleAndroidTests._none))
                    except NoSuchElementException:
                        SimpleAndroidTests._error +=1
                        log = open("../../../workspace/Appium/Android_app/MRZ_logs_error.txt", 'r+')
                        log.write("Number of attempts with errors: " + str(SimpleAndroidTests._error))
                        print ("Something gone wrong")
                try:
                    self.driver.find_element_by_id("com.paycasso.demo:id/buttonProducts").click()            
                    
                except NoSuchElementException:
                    pass
            except NoSuchElementException:
                    pass
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)