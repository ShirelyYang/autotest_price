from time import sleep

from autotest_price.price_android.price_page.base_page import BasePage


class NearbyDealers(BasePage):
    def nearby_dealers(self):
        self.find(by="xpath", locator='//*[@text="宝马"]').click()
        self.find(by="xpath", locator='//*[@text="4S-泉州晋宝宝马"]').click()
        sales_list = self.find(by="id", locator="dealer_title_txt")
        return sales_list.text

    def map(self):
        self.find(by="id", locator="tv_brand").click()
        self.base_scroll("text", "大众").click()

        # 模拟器
        # address = self.found(by="xpath", locator='//*[@content-desc="泉州展览城-东门"]')
        # return address.get_attribute(name="content-desc")

        # OPPO
        self.base_srcoll_up_down(by="xpath", locator='//*[contains(@text, "泉州大众汽车")]/..//*[@resource-id="com.yiche.price:id/iv_gps"]',
                                 rx=0.2, ry1=0.6, ry2=0.3, num=100).click()
        sleep(3)
        address = self.find(by="xpath", locator='//*[contains(@text, "泉州展览城")]')
        return address.text

    def switch_position(self):
        self.find(by="id", locator="iv_head_location").click()
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="北京"]', rx=0.2, ry1=0.3, ry2=0.6, num=100)
        self.base_srcoll_up_down(by="xpath", locator='//*[contains(@text, "福建")]', rx=0.5, ry1=0.6, ry2=0.3, num=100).click()

        self.find(by="xpath", locator='//*[@text="泉州"]').click()
        addr = self.find(by="xpath", locator='//*[contains(@text, "泉州")]/..//*[@resource-id="com.yiche.price:id/dealer_address"]')
        return addr.text
