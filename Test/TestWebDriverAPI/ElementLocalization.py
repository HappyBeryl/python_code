#元素定位
from selenium import webdriver
import time

driver = webdriver.Chrome();
driver.get("http://www.baidu.com/")
time.sleep(3)
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
time.sleep(5)
driver.quit()