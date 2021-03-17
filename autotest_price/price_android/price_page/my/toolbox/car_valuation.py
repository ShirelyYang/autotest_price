from time import sleep

from autotest_price.price_android.price_page.base_page import BasePage


class CarValuation(BasePage):
    # 爱车估值
    def car_valuation(self):
        # 选择车型
        self.find(by="id", locator="car_model_txt").click()
        self.base_scroll("text", "奔驰").click()
        self.find(by="xpath", locator='//*[@text="奔驰GLB"]').click()
        self.find(by="id", locator="title_txt").click()
        # 上牌时间
        # self.found(by="id", locator="car_onyear_txt").click()
        # self.found(by="id", locator="button1").click()
        # 里程
        self.find(by="id", locator="car_mileage_txt").send_keys("2")
        self.find(by="id", locator="et_phone").send_keys("13888888888")
        # 估价意向
        self.find(by="id", locator="tv_intention_title").click()
        sleep(3)
        self.find(by="xpath", locator='//*[contains(@text, "最近要买车")]').click()
        self.find(by="id", locator="usedcar_commit").click()
        msg = self.get_toast()
        return msg