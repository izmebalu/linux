from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import unittest
class MaheshDemo(unittest.TestCase):
    def setUp(self):
        global browser
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")

        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2
        })
        browser = webdriver.Chrome(chrome_options=option,        executable_path='/home/bharath/Downloads/chromedriver')
        browser.get('http://irctc.co.in')
        browser.maximize_window()
#    def test_1(self):
 #       browser.find_element_by_class_name('btn btn-primary').click()
        browser.find_element_by_id('pass').send_keys('oneplusnordxvr!2')
        browser.find_element_by_name('login').click()
        time.sleep(5)
        browser.find_element_by_id('userNavigationLabel').click()
        time.sleep(10)
        browser.find_element(By.CLASS,'_54nc').click()
        time.sleep(5)




if __name__ == '__main__':
    unittest
