from appium.webdriver.common.touch_action import TouchAction

from autotest_price.price_android.price_page.base_page import BasePage
from autotest_price.price_android.price_page.my.toolbox.toolbox_more import ToolBoxMore


class My(BasePage):
    def more(self):
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="更多"]', rx=0.5, ry1=0.6, ry2=0.3, num=100).click()
        return ToolBoxMore(self._driver)

    # 获取出现天气
    def get_weather(self):
        mine_weather_text = self.find(by="id", locator="mine_weather_text").text
        return mine_weather_text
