#coding=utf-8
from selenium import webdriver
from time import sleep

#driver = webdriver.PhantomJS(executable_path='/usr/local/src/phantomjs/bin/phantomjs')

#option = webdriver.ChromeOptions()
#driver = webdriver.Chrome(executable_path='/usr/local/Cellar/chromedriver/2.27/bin/chromedriver')

#option.add_argument("user-data-dir=/Users/junxiwei/Library/Application Support/Google/Chrome/Default") #设置成用户自己的数据目录
#option.add_argument("--disable-bundled-ppapi-flash")
#driver = webdriver.Chrome(executable_path='/usr/local/Cellar/chromedriver/2.27/bin/chromedriver', chrome_options=option)

driver = webdriver.Firefox(executable_path='/usr/local/Cellar/geckodriver')

driver.get("https://www.douyu.com/cold/")

sleep(10)

#print driver.get_screenshot_as_file("test.png")
print driver.find_element_by_class_name("num-v").text

driver.quit()
