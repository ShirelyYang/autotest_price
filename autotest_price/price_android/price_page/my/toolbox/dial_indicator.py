from autotest_price.price_android.price_page.base_page import BasePage


class DialIndicator(BasePage):
    # 表盘指示灯
    def dial_indicator(self):
        alarm_tv = self.find(by="id", locator="alarm_tv").text
        return alarm_tv
