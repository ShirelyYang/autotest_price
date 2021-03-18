import os

from appium import webdriver

from time import sleep

from autotest_price.price_android.price_page.base_page import BasePage
from autotest_price.price_android.price_page.found.found import Found
from autotest_price.price_android.price_page.market.market import Market
from autotest_price.price_android.price_page.my.my import My


class App(BasePage):
    _package = 'com.yiche.price'
    _activity = '.MainActivity'

    def start(self):
        # _package = 'com.yiche_android.price'

        if self._driver is None:
            sleep(3)
            caps = {}
            caps["platformName"] = "Android"
            # MUMU模拟器
            # caps["deviceName"] = "127.0.0.1:7555"
            # caps["deviceName"] = "emulator-5554"
            # OPPO手机
            # caps["deviceName"] = "c0926ab9"
            # vivo
            # caps["deviceName"] = "b724ca09"
            # OPPO
            # caps["udid"] = "c0926ab9"
            # Oppo Lulu
            caps["deviceName"] = "c4bd627c"
            # VIVO
            # caps["udid"] = "b724ca09"
            # caps["platformVersion"] = "7.1.1"
            # caps["platformVersion"] = "6.0"
            caps['automationName'] = 'UiAutomator2'
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["unicodeKeyBoard"] = "true"
            caps["resetKeyBoard"] = "true"
            caps["autoGrantPermissions"] = True
            caps["noReset"] = True
            caps['skipServerInstallation'] = True
            caps['skipDeviceInitialization'] = True
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
            self._driver.implicitly_wait(20)
        else:
            self._driver.start_activity(self._package, self._activity)
        return self

    def base_quit(self):
        f = os.popen(r"adb shell dumpsys activity top | findstr ACTIVITY", "r")  # 获取当前界面的Activity
        current_activity = f.read()
        f.close()
        print(current_activity)  # cmd输出结果

        # 用in方法 判断一个字符串是否包含某字符
        if self._package in current_activity:
            self._driver.quit()
        else:
            pass

    # 跳转至选择品牌列表
    # def main(self):
    #     return BrandList(self._driver)

    def start_stop(self):
        i = 0
        while i < 5:
            self.start()
            self.close()
            i += 1

    # 我的
    def my(self):
        self.find(by="id", locator="bottom_button05").click()
        # self.steps("../../datas/my_more_toolbox.yaml", "my")
        return My(self._driver)

    # 发现
    def found(self):
        self.find(by="id", locator="bottom_button03").click()
        return Found(self._driver)

    # 车市
    def market(self):
        self.find(by="id", locator="bottom_button04").click()
        return Market(self._driver)


