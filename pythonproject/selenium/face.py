from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import unittest
class Mahesh(unittest.TestCase):
    def setUp(self):
        global driver
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2
        })

        driver = webdriver.Chrome(chrome_options=option,        executable_path='/home/bharath/Downloads/chromedriver')
        driver.get('https://www.facebook.com')
    def test_1(self):
        driver.find_element_by_id('email').send_keys('bharath.91221@gmail.com')
        driver.find_element_by_id('pass').send_keys('oneplusnordxvr!2')
        driver.find_element_by_name('login').click()
        driver.refresh()
        driver.find_element_by_id('userNavigationLabel').click()
        driver.find_element_by_class_name('_54nc').click()
        time.sleep(5)
    def tearDown(self):
        driver.close()


if __name__ == '__main__':
    unittest
