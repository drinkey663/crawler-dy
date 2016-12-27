from selenium import webdriver
from time import sleep
driver = webdriver.PhantomJS(executable_path='/usr/local/src/phantomjs/bin/phantomjs')
driver.get("https://www.douyu.com/cold/")
#sleep(10)
#r = driver.execute_script("return readCookie")
#print r
print driver.find_element_by_class_name("num-v").text
