
from autotest_price.price_android.price_page.base_page import BasePage


class SalesRanking(BasePage):
    # 销量排行
    def sales_list(self):
        self.find(by="id", locator="car_suv_ll").click()
        self.find(by="xpath", locator='//*[@text="中大型SUV"]').click()
        self.find(by="id", locator="car_tab2").click()
        self.find(by="xpath", locator='//*[@text="25-40万"]').click()
        self.find(by="id", locator="car_tab3").click()
        self.find(by="xpath", locator='//*[@text="自主"]').click()
        # self.window_scroll(car="北京BJ80")
        self.base_scroll("text", "北京BJ80").click()
        type = self.find(by="id", locator="brandtype_serial_type")
        return type.text

    # 点评榜
    def comment_list(self):
        self.find(by="id", locator="rank_comment_tv").click()
        self.find(by="id", locator="car_tab2").click()
        self.find(by="xpath", locator='//*[@text="80万以上"]').click()
        self.find(by="id", locator="car_suv_tv").click()
        self.find(by="xpath", locator='//*[@text="中大型SUV"]').click()
        self.find(by="id", locator="car_tab3").click()
        self.find(by="xpath", locator='//*[@text="不限"]').click()
        # self.window_scroll(car="揽胜运动版")
        self.base_scroll("text", "揽胜运动版").click()
        type = self.find(by="id", locator="brandtype_serial_type")
        return type.text

    # 人气榜
    def popularity_list(self):
        self.base_scroll("text", "奔驰G级")
        self.find(by="id", locator="rank_popularity_tv").click()
        # self.base_scroll("resourceId", "rank_popularity_tv").click()
        self.find(by="id", locator="car_tab2").click()
        self.find(by="xpath", locator='//*[@text="80万以上"]').click()
        self.find(by="id", locator="car_suv_tv").click()
        self.find(by="xpath", locator='//*[@text="中大型SUV"]').click()

        # self.window_scroll(car="奔驰G级")
        self.base_scroll("text", "奔驰G级").click()
        type = self.find(by="id", locator="brandtype_serial_type")
        return type.text

    # 保值率榜
    def rank_residualratio_list(self):
        self.find(by="id", locator="rank_residualratio_tv").click()
        self.find(by="id", locator="car_suv_tv").click()
        self.find(by="xpath", locator='//*[@text="中大型SUV"]').click()
        self.find(by="xpath", locator='//*[@text="奔驰G级"]').click()
        type = self.find(by="id", locator="brandtype_serial_type")
        return type.text
