#对象的操作
import os

from selenium import webdriver
import time


from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.find_element_by_id("kw").send_keys("白琼")
driver.sleep(5)
driver.find_element_by_id("su").click()

# file_path = 'file:///' + os.path.abspath("D://code")
# driver.get(file_path)
# driver.maximize_window()
# inputs = driver.find_elements_by_tag_name("input") #找出所有的input元素
# time.sleep(6)
# for input in inputs:
#     if input.get_attribute('type') == "checkbox":
#         input.click()






# driver.maximize_window()

# time.sleep(10)
# driver.quit()
# ActionChains(driver).double_click(su1).perform()
# time.sleep(6)

# title = driver.find_element_by_id("su") #原位置
# target = driver.find_element_by_link_text("乃万_百度百科") #现位置
# ActionChains(driver).drag_and_drop(title, target).perform()  #拖动
# ActionChains(driver).move_to_element(title, target).perform()  #移动

# ActionChains(driver).double_click(su1).perform()
# driver.get("https://mail.163.com/")
# time.sleep(5)
# driver.find("auto-id-1593653751095").send_keys("51398")
# driver.find_element_by_id("auto-id-1593653751095").send_keys(Keys.TAB)
# driver.find_element_by_id("auto-id-1593653751098").send_keys("1234567b")
# time.sleep(3)
# driver.find_element_by_id("auto-id-1593653751098").send_keys(Keys.ENTER)
#driver.maximize_window()
#driver.minimize_window()
# time.sleep(5)
# driver.find_element_by_id("kw").send_keys("莫言")
# driver.find_element_by_id("su").click()
# driver.maximize_window()
# time.sleep(8)

#将页面滚动条拖到底部
# js="var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js)
# time.sleep(3)
#将滚动条移动到页面的顶部
# js="var q=document.documentElement.scrollTop=0"
# driver.execute_script(js)
# time.sleep(3)
# driver.quit()

#driver.back()
#driver.forward()
#
# driver.find_element_by_id("kw").clear()
# time.sleep(8)
#
# driver.find_element_by_id("kw").send_keys("匪我思存")
# driver.find_element_by_id("su").submit()
# time.sleep(8)

# t=driver.find_element_by_id("s-bottom-layer-right").text
# print(t)
#
# title=driver.title
# print(title)
#
# url = driver.current_url
# print(url)

#driver.set_window_size(400,200)