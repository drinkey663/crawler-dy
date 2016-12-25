from selenium import webdriver
driver = webdriver.PhantomJS(executable_path='/usr/local/src/phantomjs/bin/phantomjs')
driver.get("http://www.huomao.com/666666/")

#r = driver.execute_script("return readCookie")
#print r

print driver.find_element_by_id("watching-view").text
