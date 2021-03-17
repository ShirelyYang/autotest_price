from time import sleep

from autotest_price.price_android.price_page.base_page import BasePage

class BorrowCash(BasePage):
    def borrow_cash(self):
        sleep(3)
        title_center_txt = self.find(by="id", locator="title_center_txt").text
        return title_center_txt
