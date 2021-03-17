
from time import sleep

from autotest_price.price_android.price_page.base_page import BasePage


class Calculator(BasePage):
    def cal(self):
        self.find(by="id", locator="carNameTxt").click()
        # self.steps("../../../../datas/my_more_toolbox.yaml", "cal")
        sleep(3)
        self.find(by="id", locator="searchEdtTxt").click()
        self.find(by="id", locator="searchEt").send_keys("宝马X3")
        # self.found(by="xpath", locator='//*[@text="奔驰GLC"]').click()
        self.find(by="id", locator="txtView").click()
        self.find(by="xpath", locator="//*[@text='宝马X3']").click()
        # price = self.found(by="xpath", locator='//*[@text="35.38万起"]').text
        self.find(by="xpath", locator="//*[contains(@text, '运动套装')]").click()
        calculateBtn = self.find(by="id", locator="carcalculate_byfy_title_txt")
        return calculateBtn.text

    # 贷款页面
    def loan(self):
        # if self.cal() is None:
        #     self.cal()
        self.find(by="id", locator="loanBtn").click()
        contains = self.find(by="xpath", locator='//*[@text="首付比例"]')
        return contains.text

    # 重置
    def reset(self):
        # if self.cal() is None:
        #     self.cal()
        self.find(by="id", locator="title_right_btn").click()
        btn_clear = self.find(by="id", locator="calculate_history_clear")
        return btn_clear.text