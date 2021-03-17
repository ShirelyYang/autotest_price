
from autotest_price.price_android.price_page.base_page import BasePage


class DealPrice(BasePage):
    # 选择车型
    def select_car(self):
        self.find(by="id", locator="serial_sel").click()
        self.find(by="id", locator="searchEdtTxt").click()
        self.find(by="id", locator="searchEt").send_keys("宝马X3")
        self.find(by="xpath", locator='//*[@resource-id="com.yiche.price:id/txtView" and @text="宝马X3"]').click()
        self.find(by="xpath", locator='//*[@text="宝马X3"]').click()

    # 列表选车
    def list_car_selection(self):
        self.base_scroll("text", "哈弗H6").click()

    # 成交价格
    def deal_price(self):
        # self.select_car()
        self.list_car_selection()
        self.find(by="id", locator="other_city_name").click()
        self.base_scroll("text", "北京").click()
        # self.found(by="xpath", locator='//*[@resource-id="com.yiche.price:id/nearby_city_name" and @text="北京"]').click()
        self.find(by="xpath", locator='//*[@text="全部车款"]').click()
        self.find(by="xpath", locator='//*[contains(@text, "都市版")]').click()
        self.find(by="xpath", locator='//*[@resource-id="com.yiche.price:id/op_progress"]//*[contains(@text, "都市版")]').click()
        luoche_price = self.find(by="id", locator="luoche_price")
        return luoche_price.text

    # 询底价
    def ask_price(self):
        # self.select_car()
        self.find(by="id", locator="owner_ask_price_btn").click()
        askprice_btn = self.find(by="id", locator="askprice_txt_bottom")
        return askprice_btn.text

    # 其他城市
    def other_city(self):
        # self.list_car_selection()
        self.find(by="id", locator="other_city_name").click()
        # self.found(by="xpath", locator='//*[@text="淮北"]').click()
        self.base_scroll("text", "武汉").click()
        city = self.find(by="id", locator="loction")
        return city.text

    # 查看发票
    def invoice(self):
        # self.select_car()
        # self.list_car_selection()
        # self.found(by="xpath", locator='//*[@resource-id="com.yiche.price:id/nearby_city_name" and @text="北京"]').click()
        # self.found(by="xpath", locator='//*[@text="查看发票"]').click()

        self.find(by="id", locator="other_city_name").click()
        self.base_scroll("text", "北京").click()
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="查看发票"]',
                                 rx=0.5, ry1=0.6, ry2=0.3, num=100).click()
        # self.base_scroll("text", "查看发票").click()
        img = self.find(by="id", locator="pv_img")
        return img.is_enabled()

    # 说明
    def description(self):
        # self.list_car_selection()
        self.find(by="id", locator="shuoming_txt").click()
        msg = "非发票形式获取，仅供参考"
        toast_msg = f'//*[@text="{msg}"]'
        toast_ele = self.find(by="xpath", locator=toast_msg)
        return toast_ele.text

    # 落地价-全款
    def full_amount(self):
        # self.list_car_selection()
        # self.found(by="xpath", locator='//*[@resource-id="com.yiche.price:id/nearby_city_name" and @text="北京"]').click()
        # self.found(by="xpath", locator='//*[@text="全部车款"]').click()
        # self.found(by="xpath", locator='//*[contains(@text, "都市版")]').click()

        self.find(by="id", locator="other_city_name").click()
        self.base_scroll("text", "廊坊").click()
        # self.found(by="xpath", locator='//*[@text="廊坊"]').click()
        # self.base_srcoll_window(by="id", locator="tv_calculate")
        # self.base_swipe()
        # self.base_scroll("resourceId", "tv_calculate").click()
        self.find(by="id", locator="tv_calculate").click()
        fullPaymentTxt = self.find(by="id", locator="fullPaymentTxt").text
        self.back()
        total_price = self.find(by="id", locator="total_price").text
        return total_price, fullPaymentTxt

    # 落地价-贷款
    def loan(self):
        self.base_srcoll_up_down(by="id", locator="tv_calculate_loan",
                                 rx=0.5, ry1=0.6, ry2=0.3, num=100).click()
        zjTxt = self.find(by="id", locator="zjTxt").text
        self.back()
        total_price_loan = self.find(by="id", locator="total_price_loan").text
        return total_price_loan, zjTxt

    # 保值率
    def rate(self):
        self.list_car_selection()
        self.find(by="xpath", locator='//*[@resource-id="com.yiche.price:id/nearby_city_name" and @text="北京"]').click()
        self.find(by="xpath", locator='//*[@text="全部车款"]').click()
        self.find(by="xpath", locator='//*[contains(@text, "都市版")]').click()
        self.find(by="xpath", locator='//*[@text="廊坊"]').click()

        self.find(by="xpath", locator='//*[@class="android.widget.LinearLayout"]').click()
        # 点击查看完整榜单
        self.base_srcoll_up_down(by="id", locator="tv_ranking",
                                 rx=0.5, ry1=0.6, ry2=0.3, num=100).click()
        # 在保值率榜单页面选择SUV-紧凑型SUV
        self.find(by="id", locator="car_suv_tv").click()
        self.find(by="xpath", locator='//*[@text="紧凑型SUV"]').click()
        self.base_scroll("text", "哈弗H6")
        sales_ratio_tv = self.find(by="id", locator="sales_ratio_tv").text
        self.back()
        # 在成交价页面查看保值率
        rate = self.find(by="id", locator="residualratio_years").text
        return sales_ratio_tv, rate





