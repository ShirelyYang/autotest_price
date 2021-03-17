from time import sleep

from autotest_price.price_android.price_page.base_page import BasePage


class BeautyChooseCar(BasePage):
    def beauty_choose_car(self):
        sleep(3)
        # 从相册选照片
        self.find(by="id", locator="picalbum").click()
        self.find(by="id", locator="media_thumbnail").click()
        self.find(by="id", locator="tv_submit").click()
        sleep(3)
        info = self.finds(by="xpath", locator='//*[@class="android.widget.TextView"]')[0].text
        self.back()
        self.find(by="id", locator="back").click()
        return info