
from appium import webdriver
import os
import unittest
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        """Swipe from one point to another point, for an optional duration.

        :Args:
         - start_x - x-coordinate at which to start
         - start_y - y-coordinate at which to start
         - end_x - x-coordinate at which to stop
         - end_y - y-coordinate at which to stop
         - duration - (optional) time to take the swipe, in ms.

        :Usage:
            driver.swipe(100, 100, 100, 400)
        """
        # `swipe` is something like press-wait-move_to-release, which the server
        # will translate into the correct action
        action = TouchAction(self)
        action \
            .press(x=start_x, y=start_y) \
            .wait(ms=duration) \
            .move_to(x=end_x, y=end_y) \
            .release()
        action.perform()
        return self

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
        self.driver.implicitly_wait(100)
     
    def tearDown(self):
        # end session
        self.driver.quit()   
     
    def test_login_offline(self):
        #Turn OFF WIFI
        
        
        url = self.driver.find_element_by_id("com.paycasso.demo:id/editUrl")
        if url.is_displayed():
            url.send_keys('auth.paycasso.com')
            
            self.driver.swipe(534, 50, 542, 1750)
            
            self.driver.switch_to_alert()
            
            self.driver.find_element_by_accessibility_id("Settings").click() #settings button

            #self.driver.find_element_by_accessibility_id("Tap to select a network").click()

            positions = []
            positions.append((972, 612)) 
            self.driver.tap(positions)
            
            self.driver.back()
            
            #self.driver.find_element_by_id('com.android.settings:id/switchWidget').click() #wifi on/off click
            
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
            assert not auth

    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Login)
    unittest.TextTestRunner(verbosity=2).run(suite)