
from appium import webdriver
import os
import unittest

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Login(unittest.TestCase):
    
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            '../../../workspace/Appium/Android_app/app-debug.apk'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(1000)
     
    def tearDown(self):
        # end session
        self.driver.quit()   
     
    def test_happy_pass(self):
        url = self.driver.find_element_by_id("com.paycasso.demo:id/editUrl")
        if url.is_displayed():
            url.send_keys('auth.paycasso.com')
            
            #Set Login 
            
            login = self.driver.find_element_by_id("com.paycasso.demo:id/editConsumer")
            login.click()
            login.send_keys('sa') 
        
            self.driver.back()
            
            #Set password
            
            password = self.driver.find_element_by_id('com.paycasso.demo:id/editPassword')
            password.click()
            password.send_keys('verify10') 

            self.driver.back()
            
            #Click Authorize
            
            self.driver.find_element_by_id("com.paycasso.demo:id/btnAuthorize").click() 
        
            Docu = self.driver.find_element_by_id('com.paycasso.demo:id/buttonDocuSure').is_displayed()
            assert Docu
        
           
    def test_login_non_existed_url(self):
        url = self.driver.find_element_by_id("com.paycasso.demo:id/editUrl")
        if url.is_displayed():
            url.send_keys('auth.paycasso.co')
            
            #Set Login 
            
            login = self.driver.find_element_by_id("com.paycasso.demo:id/editConsumer")
            login.click()
            login.send_keys('sa') 
        
            self.driver.back()
            
            #Set password
            
            password = self.driver.find_element_by_id('com.paycasso.demo:id/editPassword')
            password.click()
            password.send_keys('verify10') 

            self.driver.back()
            
            #Click Authorize
            
            self.driver.find_element_by_id("com.paycasso.demo:id/btnAuthorize").click() 
        
            auth = self.driver.find_element_by_id('com.paycasso.demo:id/btnAuthorize').is_displayed()
            assert auth
        
          
    def test_login_non_existed_user(self):
        url = self.driver.find_element_by_id("com.paycasso.demo:id/editUrl")
        if url.is_displayed():
            url.send_keys('auth.paycasso.com')
            
            #Set Login 
            
            login = self.driver.find_element_by_id("com.paycasso.demo:id/editConsumer")
            login.click()
            login.send_keys('scrum') 
        
            self.driver.back()
            
            #Set password
            
            password = self.driver.find_element_by_id('com.paycasso.demo:id/editPassword')
            password.click()
            password.send_keys('verify10') 

            self.driver.back()
            
            #Click Authorize
            
            self.driver.find_element_by_id("com.paycasso.demo:id/btnAuthorize").click() 
            
            auth = self.driver.find_element_by_id('com.paycasso.demo:id/btnAuthorize').is_displayed()
            assert auth
            
            
    def test_login_incorrect_password(self):
        url = self.driver.find_element_by_id("com.paycasso.demo:id/editUrl")
        if url.is_displayed():
            url.send_keys('auth.paycasso.com')
            
            #Set Login 
            
            login = self.driver.find_element_by_id("com.paycasso.demo:id/editConsumer")
            login.click()
            login.send_keys('sa') 
        
            self.driver.back()
            
            #Set password
            
            password = self.driver.find_element_by_id('com.paycasso.demo:id/editPassword')
            password.click()
            password.send_keys('verify101') 

            self.driver.back()
            
            #Click Authorize
            
            self.driver.find_element_by_id("com.paycasso.demo:id/btnAuthorize").click()  
            
            auth = self.driver.find_element_by_id('com.paycasso.demo:id/btnAuthorize').is_displayed()
            assert auth
             
    def test_login_offline(self):
        #Turn OFF WIFI
        self.driver.swipe(start=75, starty=500, endx=75, endy=0, duration=800)
        
        url = self.driver.find_element_by_id("com.paycasso.demo:id/editUrl")
        if url.is_displayed():
            url.send_keys('auth.paycasso.com')
            
            #Set Login 
            
            login = self.driver.find_element_by_id("com.paycasso.demo:id/editConsumer")
            login.click()
            login.send_keys('sa') 
        
            self.driver.back()
            
            #Set password
            
            password = self.driver.find_element_by_id('com.paycasso.demo:id/editPassword')
            password.click()
            password.send_keys('verify10') 

            self.driver.back()
            
            #Click Authorize
            
            self.driver.find_element_by_id("com.paycasso.demo:id/btnAuthorize").click() 
        
            auth = self.driver.find_element_by_id('com.paycasso.demo:id/btnAuthorize').is_displayed()
            assert auth

    def test_login_with_offline_transactions(self):
        pass

    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Login)
    unittest.TextTestRunner(verbosity=2).run(suite)