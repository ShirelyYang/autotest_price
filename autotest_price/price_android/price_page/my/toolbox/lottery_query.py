from time import sleep

from autotest_price.price_android.price_page.base_page import BasePage


class LotteryQuery(BasePage):
    # 增加摇号信息
    def add(self, name, number):
        self.find(by="id", locator="lpla_et_name").send_keys(name)
        self.find(by="id", locator="lpla_et_num").send_keys(number)
        self.find(by="id", locator="lpla_tv_search").click()
        sleep(3)
        name_query = self.find(by="id", locator="lpl_item_tv_name").text
        number_query = self.find(by="id", locator="lpl_item_tv_num").text
        return name, name_query, number, number_query
