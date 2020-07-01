#对象的操作
from selenium import webdriver
import time

driver = webdriver.Chrome();
driver.get("http://www.baidu.com/")
time.sleep(3)
# driver.find_element_by_id("kw").send_keys("莫言")
# driver.find_element_by_id("su").click()
# time.sleep(8)
#
# driver.find_element_by_id("kw").clear()
# time.sleep(8)
#
# driver.find_element_by_id("kw").send_keys("匪我思存")
# driver.find_element_by_id("su").submit()
# time.sleep(8)

t=driver.find_element_by_id("s-bottom-layer-right").text
print(t)



