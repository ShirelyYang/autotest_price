from autotest_price.price_android.price_page.base_page import BasePage
from autotest_price.price_android.price_page.found.headlines.headlines import Headlines
from autotest_price.price_android.price_page.found.live_broadcast.live_broadcast import LiveBroadcast
from autotest_price.price_android.price_page.found.original.original import Original
from autotest_price.price_android.price_page.found.small_video.small_video import SmallVideo
from autotest_price.price_android.price_page.found.square.square import Square
from autotest_price.price_android.price_page.found.video.video import Video
from autotest_price.price_android.price_page.found.yiche_number.yiche_number import YicheNumber


class Found(BasePage):
    # 头条
    def goto_headlines(self):
        self.find(by="xpath", locator='//*[@text="头条"]').click()
        return Headlines(self._driver)

    # 小视频
    def goto_small_video(self):
        self.find(by="xpath", locator='//*[@text="小视频"]').click()
        return SmallVideo(self._driver)

    # 原创
    def goto_original(self):
        self.find(by="xpath", locator='//*[@text="原创"]').click()
        return Original(self._driver)

    # 直播
    def goto_live_broadcast(self):
        # self.find(by="xpath", locator='//*[@text="直播"]').click()
        self.base_scroll_left_right(by="xpath", locator='//*[@text="直播"]', ry=0.2, rx1=0.8, rx2=0.2, num=100).click()
        return LiveBroadcast(self._driver)

    # 视频
    def goto_video(self):
        # self.find(by="xpath", locator='//*[@text="直播"]').click()
        self.base_scroll_left_right(by="xpath", locator='//*[@text="视频"]', ry=0.2, rx1=0.8, rx2=0.2, num=100).click()
        return Video(self._driver)

    # 易车号
    def goto_yiche_number(self):
        # self.find(by="xpath", locator='//*[@text="直播"]').click()
        self.base_scroll_left_right(by="xpath", locator='//*[@text="易车号"]', ry=0.2, rx1=0.8, rx2=0.2, num=100).click()
        return YicheNumber(self._driver)

    # 广场
    def goto_square(self):
        self.base_scroll_left_right(by="xpath", locator='//*[@text="广场"]', ry=0.2, rx1=0.8, rx2=0.2, num=100).click()
        return Square(self._driver)

