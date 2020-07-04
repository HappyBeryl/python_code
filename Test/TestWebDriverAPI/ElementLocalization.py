#元素定位
import os

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("Jay")
driver.maximize_window()
time.sleep(8)

 #将页面滚动条拖到底部
# js="var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js)
# time.sleep(8)

#将滚动条移动到页面的顶部
# js="var q=document.documentElement.scrollTop=0"
# driver.execute_script(js)
# time.sleep(8)
# driver.set_window_size(400, 800)
# time.sleep(8)

#同时控制浏览器的左右、上下。从左向右偏离200，从上向下偏离200
# js = "window.scrollTo(100, 200)"
# driver.execute_script(js)
# time.sleep(8)

# file_path = 'file///'+ os.path.abspath("D:\\code\\Test.py")
# driver.get(file_path)
# driver.switch_to.frame("f1")
# driver.switch_to.frame("f2")
# driver.find_element_by_id("kw").send_keys("布拉格")
# driver.find_element_by_id("su").click()
# time.sleep(8)
#
# #如果要跳转到f1
# driver.switch_to_default_content()
# driver.switch_to_frame("f1")
#
# driver.quit()
# driver.get("http://www.baidu.com/")
# driver.find_element_by_id("kw").send_keys("白琼")
# driver.sleep(5)
# driver.find_element_by_id("su").click()
# time.sleep(10)
#driver.find_element_by_id("kw").send_keys("哆啦A梦")  id进行定位

#driver.find_element_by_name("wd").send_keys("海绵宝宝") name进行定位
#driver.find_element_by_id("su").click()

#driver.find_element_by_class_name("s_ipt").send_keys("派大星") class name进行定位
#driver.find_element_by_class_name("btn self-btn bg s_btn").click()

#driver.find_element_by_link_text("抗击疫情").click()  link text进行定位（链接定位）

#driver.find_element_by_partial_link_text("疫情").click() partial link text进行定位(部分链接定位)

#无法定位，只有input在页面是唯一的才可定位
#driver.find_element_by_tag_name("input").send_keys("功夫小子") tag name进行定位（标签名字定位）

#driver.find_element_by_xpath("//*[@id='kw']").send_keys("喜羊羊")  xpath进行定位（路径定位）
#driver.find_element_by_xpath("//*[@id='su']").click()

#driver.find_element_by_css_selector("#kw").send_keys("灰太狼")  css selector进行定位（css样式定位）

# driver.quit()