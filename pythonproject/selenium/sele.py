from selenium import webdriver
driver=webdriver.Chrome(executable_path='/home/bharath/Downloads/chromedriver')
driver.get('http://www.facebook.com')
driver.maximize_window()
print("Title is:",driver.title)
print("current url:",driver.current_url)
driver.find_element_by_id('email').send_keys('bharath.91221@gmail.com')
driver.find_element_by_id('pass').send_keys('oneplus5Tvr!2')
driver.find_element_by_name('login').click()
