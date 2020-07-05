from ddt import ddt, data, unpack ,file_data


# import unittest
# from selenium import webdriver
# import time
# class Baidu1(unittest.TestCase):
#     def SetUp(self):
#         self.driver = webdriver.chrome()
#         self.driver.implicitly_wait(30)
#         self.base_url = "http://www.baidu.com/"
#         self.driver.maximize_window()
#         self.verificationErrors = []
#         self.accept_next_alert = True
#     def tearDown(self):
#         self.driver.quit()
#         self.assertEqual([],self.verificationErrors)
#     def test_baidusearch(self):
#         driver = self.driver
#         driver.get(self.base_url)
#         driver.find_element_by_id("kw").clear()
#         driver.find_element_by_id("kw").send_keys("这个杀手不太冷")
#         driver.find_element_by_id("su").click()
#         time.sleep(6)

# import unittest, csv
# import os, sys
# import time
# import HTMLTestRunner
#
#
# # 手工添加案例到套件，
# def createsuite():
#     discover = unittest.defaultTestLoader.discover('../test', pattern='test*.py', top_level_dir=None)
#     print(discover)
#     return discover
# if __name__ == "__main__":
#     #1.创建文件夹
#     #sys.path是python搜索模块的路径集，返回的结果是一个list
#     curpath = sys[0]
#     if not os.path.exists(curpath+'/resultreport'):
#         os.mkdir(curpath+'/resultreport')
#
#     #2.创建文件，以当前时间命名
#     now = time.strftime("%Y-%m-%d-%H %M %S", time.localtime(time.time()))
#     filename = curpath + '/resultreport' + now + 'resultreport.html'
#     #3.打开文件，进行获取html报告
#     with open(filename, 'wb') as fp:
#         runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况',verbosity=2)
#         suite = createsuite()
#         runner.run(suite)


    # def savescreenshot(self, driver, file_name):
    #     if not os.path.exists('./image'):
    #         os.makedirs('./image')
    #
    #
    # now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
    # # 截图保存
    # driver.get_screenshot_as_file('./image/' + now + '-' + file_name)
    # time.sleep(1)