from autotest_price.price_android.price_page.base_page import BasePage


class PriceCutRanking(BasePage):
    # 条件筛选
    def conditions(self):
        # 车型
        self.find(by="id", locator="promotion_car_type_txt").click()
        self.base_scroll("text", "奔驰").click()
        self.find(by="xpath", locator='//*[contains(@text, "奔驰GLC")]').click()
        # 价格
        self.find(by="id", locator="promotion_price_selector_txt").click()
        self.find(by="xpath", locator='//*[contains(@text, "30–50万")]').click()
        # 级别
        self.find(by="id", locator="promotion_car_selector_txt").click()
        self.find(by="xpath", locator='//*[contains(@text, "SUV")]').click()
        # 降幅最大
        self.find(by="id", locator="promotion_biggest_decline_txt").click()
        self.find(by="xpath", locator='//*[contains(@text, "价格最高")]').click()
        # 点击筛选结果中的第一条数据并获取其名称
        # # car_name = self.found(by="id", locator="promotionrank_title")
        # car_names = self.finds(by="xpath", locator='//*[contains(@text, "奔驰GLC ")]')
        # car_name = car_names[2]
        car_name = self.find(by="xpath", locator='//*[contains(@text, "奔驰GLC ")]')
        car_name.click()
        brandType_title = self.find(by="id", locator="brandType_title")
        return car_name.text, brandType_title.text

    # 贷款
    def loan(self):
        self.find(by="id", locator="promotion_focus_dial").click()
        btn = self.find(by="id", locator="submit")
        return btn.text

    # 提交贷款
    def submit_loan(self):
        self.find(by="id", locator="ask_name").send_keys("测试")
        self.find(by="id", locator="ask_tel").send_keys("13588888888")
        self.find(by="id", locator="submit").click()
        toast = self.get_toast()
        return toast

    # 询底价
    def ask_price(self):
        self.find(by="id", locator="promotion_focus_loan").click()
        self.find(by="id", locator="ask_name").send_keys("测试")
        self.find(by="id", locator="ask_tel").send_keys("13588888888")
        self.find(by="id", locator="askprice_txt_bottom").click()
        fapr_tv_title = self.find(by="id", locator="fapr_tv_title").text
        self.find(by="id", locator="fapr_iv_close").click()
        return fapr_tv_title

    # 400电话
    def tel(self):
        self.find(by="id", locator="promotion_focus_askprice").click()
        alertTitle = self.find(by="id", locator="alertTitle").text
        self.find(by="id", locator="button1").click()
        return alertTitle

    # 清空
    def clear(self):
        self.find(by="id", locator="clear_history_tv").click()
        try:
            self.find(by="id", locator="clear_history_tv").click()
        except Exception as e:
            msg = "页面不存在清空元素"
            print(msg)

    # 切换城市
    def change_city(self):
        self.find(by="id", locator="title_right_btn").click()
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="北京"]', rx=0.2, ry1=0.3, ry2=0.6, num=100)
        # self.base_scroll("text", "江苏").click()
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="江苏"]', rx=0.5, ry1=0.6, ry2=0.4, num=100).click()
        self.find(by="xpath", locator='//*[@text="南京"]').click()
        addr = self.find(by="id", locator="promotionrank_is4s").text
        return addr

    # 批量询价
    def ask_price_all(self):
        self.find(by="id", locator="promitionrank_commit").click()
        radios = self.finds(by="id", locator="dealer_select")
        for i in range(3):
            radios[i].click()
        self.find(by="id", locator="promitionrank_commit").click()
        self.find(by="id", locator="et_name").send_keys("测试")
        self.find(by="id", locator="et_phone").send_keys("13888888888")
        self.find(by="id", locator="check_login_view").click()
        self.find(by="id", locator="commit1").click()
        toast = self.get_toast()
        return toast