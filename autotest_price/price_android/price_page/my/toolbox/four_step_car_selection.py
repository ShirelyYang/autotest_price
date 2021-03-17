from time import sleep

from autotest_price.price_android.price_page.base_page import BasePage


class FourStepCarSelection(BasePage):
    def scroll_one_step(self, param):
        self.base_srcoll_up_down(by="xpath", locator=f'//*[@text="{param}"]',
                                 rx=0.5, ry1=0.6, ry2=0.4, num=100).click()

    def determine_needs(self):
        self.find(by="xpath", locator='//*[@text="女"]').click()
        self.find(by="xpath", locator='//*[@text="90后"]').click()
        self.scroll_one_step("新手上路")
        self.find(by="id", locator="tv_choose_car_commit").click()
        self.find(by="xpath", locator='//*[@text="暂不考虑"]').click()
        self.find(by="id", locator="tv_choose_car_commit").click()
        self.find(by="xpath", locator='//*[@text="大块头suv"]').click()
        sleep(5)
        btn = self.find(by="id", locator="tv_choose_car_commit")
        btn.click()

    def one_step(self):
        self.find(by="id", locator="tv_step_1").click()
        sleep(3)
        try:
            btn = self.find(by="id", locator="tv_choose_car_commit")
            if "符合要求" in btn.text:
                self.find(by="xpath", locator='//*[@text="大块头suv"]').click()
                self.find(by="id", locator="up_tv").click()
                self.find(by="xpath", locator='//*[@text="暂不考虑"]').click()
                self.find(by="id", locator="up_tv").click()
                self.scroll_one_step("新手上路")
                self.scroll_one_step("女")
                self.find(by="xpath", locator='//*[@text="90后"]').click()
                self.find(by="xpath", locator='//*[@text="90后"]').click()
                self.find(by="xpath", locator='//*[@text="女"]').click()
                self.scroll_one_step("新手上路")
                sleep(3)
                self.find(by="id", locator="tv_choose_car_commit").click()
                # btn.click()
                sleep(3)
                self.find(by="id", locator="tv_choose_car_commit").click()
                # btn.click()
                sleep(10)
                self.find(by="id", locator="tv_choose_car_commit").click()
                # btn.click()
            elif "3/3" in self.find(by="id", locator="title").text:
                self.find(by="xpath", locator='//*[@text="大块头suv"]').click()
                btn.click()
            elif "2/3" in self.find(by="id", locator="title").text:
                self.find(by="xpath", locator='//*[@text="暂不考虑"]').click()
                # self.found(by="id", locator="tv_choose_car_commit").click()
                btn.click()
                self.find(by="xpath", locator='//*[@text="大块头suv"]').click()
                btn.click()
            else:
                self.determine_needs()
        except Exception as e:
            self.determine_needs()

    def two_step(self):
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="宝马X7"]',
                                 rx=0.5, ry1=0.8, ry2=0.3, num=100).click()
        btn = self.find(by="id", locator="tv_choose_car_commit")
        btn.click()

    def three_step(self):
        self.base_scroll_left_right(by="xpath", locator='//*[contains(@text, "运动套装")]',
                                    rx1=0.8, rx2=0.2, ry=0.5).click()
        btn = self.find(by="id", locator="tv_intelligent3_car_commit")
        btn.click()

    def four_step(self):
        self.find(by="id", locator="promotion_focus_askprice").click()

    def four_steps(self):
        self.one_step()
        self.two_step()
        self.three_step()
        self.four_step()
        ask_price_btn = self.find(by="id", locator="askprice_txt_bottom")
        return ask_price_btn.text
