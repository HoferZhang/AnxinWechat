# -*- coding: utf-8 -*-


from appium import webdriver
import unittest
import time


class AxDoc(unittest.TestCase):
    def setUp(self):
        packageName = 'com.tencent.mm'
        appActivity = '.ui.LauncherUI'

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = 'c30ee021'
        desired_caps['appPackage'] = packageName
        desired_caps['appActivity'] = appActivity
        desired_caps['fullReset'] = 'false'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['fastReset'] = 'false'
        desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}  # 驱动H5自动化关键之一

        self.driver = webdriver.Remote('http://127.0.1.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()

    def test_1_login(self):
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
        print self.driver.current_context
        print self.driver.page_source
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('我的医生').click()
        # print self.driver.contexts
        # self.driver.find_element_by_name('相册').click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'正在繁星直播')]").click()
        # print self.driver.current_context
        # self.driver.find_element_by_xpath("//*[contains(@text,'正在繁星直播')]").click()
        # print self.driver.current_context
        # self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
        # print self.driver.current_context
        # print self.driver.page_source
        # self.driver.find_element_by_xpath('//*[@id="btnRecommend"]/div[1]').click()
        # self.driver.switch_to_default_content()
        time.sleep(2)
        self.driver.quit()


# unitest.main()函数用来测试 类中以test开头的测试用例
if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(AxDoc)
    unittest.TextTestRunner(verbosity=3).run(suite)