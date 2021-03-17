from time import sleep

from autotest_price.price_android.price_page.base_page import BasePage


class CarReplacement(BasePage):
    # 二手车置换
    def car_replacement(self):
        self.find(by="id", locator="askpirce_city_txt").click()
        sleep(3)
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="北京"]', rx=0.2, ry1=0.2, ry2=0.8, num=100)
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="甘肃"]', rx=0.5, ry1=0.6, ry2=0.3, num=100).click()
        self.find(by="xpath", locator='//*[@text="兰州"]').click()
        self.find(by="id", locator="et_phone").send_keys("13888888888")
        self.find(by="id", locator="commit1").click()
        sleep(3)
        msg_list = ["提交成功", "网络不给力哦，请重试"]
        try:
            msg = self.find(by="id", locator="title").text
            self.find(by="id", locator="cancel").click()
        except Exception as e:
            msg = self.get_toast()
        return msg, msg_list

