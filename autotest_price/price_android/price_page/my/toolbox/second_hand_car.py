from appium.webdriver.common.mobileby import MobileBy

from autotest_price.price_android.price_page.base_page import BasePage


class SecondHandCar(BasePage):
    # 条件筛选
    def condition(self):
        self.find(by="id", locator="title_right").click()
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="北京"]', rx=0.2, ry1=0.3, ry2=0.6, num=100)
        # self.scroll_window("广东")
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="广东"]', rx=0.5, ry1=0.7, ry2=0.3, num=100).click()
        self.find(by="xpath", locator='//*[contains(@text, "深圳")]').click()
        # 选择品牌
        self.find(by="id", locator="car_models").click()
        # 滚动查找 “路虎”
        brand = self.base_scroll("text", "路虎")
        brand.click()
        # 选择车款
        self.find(by="xpath", locator='//*[@text="揽胜极光(进口)"]').click()
        # # 选择价格
        # self.found(by="id", locator="car_price").click()
        # self.found(by="xpath", locator='//*[@text="15-20万"]').click()
        # # 选择车龄
        # self.found(by="id", locator="car_years").click()
        # self.found(by="xpath", locator='//*[@text="5-8年"]').click()
        # 筛选
        self.find(by="xpath", locator='//*[@text="筛选"]').click()
        self.find(by="xpath", locator='//*[@text="10万公里内"]').click()
        self.find(by="xpath", locator='//*[@text="SUV"]').click()
        self.find(by="xpath", locator='//*[@text="商家"]').click()
        # # self.window_scroll(attr="xpath", locate='//*[@text="自动挡"]')
        # sleep(2)
        # self.found(by="xpath", locator='//*[@text="全部"]').click()
        self.base_scroll("text", "国5").click()
        self.base_srcol("text", "1.6-2.0L").click()
        self.find(by="id", locator="ok").click()
        # self.scroll("resourceId", "com.yiche.price:id/ok").click()
        # 选择筛选结果
        self.find(by="xpath", locator='//*[contains(@text, "2014款")]').click()
        # 获取综述页车型标题
        title = self.find(by="id", locator="fulTvName").text
        return title

    # 切换城市
    def change_city(self):
        self.find(by="id", locator="title_right").click()
        # self.scroll("text", "辽宁").click()
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="北京"]', rx=0.2, ry1=0.3, ry2=0.6, num=100)
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="辽宁"]', rx=0.5, ry1=0.6, ry2=0.3, num=100).click()
        self.find(by="xpath", locator='//*[contains(@text, "沈阳")]').click()
        self.find(by="id", locator="title_extra_search_layout").click()
        self.find(by="id", locator="searchEt").send_keys("天籁")
        self.find(by="id", locator="txtView").click()
        ele = self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable('
                                                                          'new UiSelector().scrollable(true)'
                                                                          '.instance(0)).scrollIntoView('
                                                                          'new UiSelector().textContains("天籁 2013款 2.5XL")'
                                                                          f'.instance(0));')
        addr = self.find(by="xpath", locator='//*[contains(@text, "天籁 2013款 2.5XL")]/../*[contains(@text, "沈阳")]').text
        return addr

    # 清空
    def clear(self):
        # self.condition()
        self.find(by="xpath", locator='//*[@text="清空"]').click()
        try:
            self.find(by="xpath", locator='//*[@text="清空"]').click()
        except Exception as e:
            msg = "页面不存在清空元素"
            print(msg)
