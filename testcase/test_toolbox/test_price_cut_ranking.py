from autotest_price.price_android.price_page.app import App


class TestPriceCutRanking:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_price_cut_ranking()

    def setup(self):
        pass

    def teardown_class(self):
        self.app.base_quit()

    def teardown(self):
        pass

    # 条件选车
    def test_conditions(self):
        car_name, brandType_title = self.main.conditions()
        assert car_name == brandType_title
        self.app.back()

    # 贷款
    def test_loan(self):
        btn = self.main.loan()
        assert "贷款" in btn

    # 提交贷款
    def test_submit_loan(self):
        toast = self.main.submit_loan()
        assert toast == "提交成功"

    # 询底价
    def test_ask_price(self):
        fapr_tv_title = self.main.ask_price()
        assert fapr_tv_title == "询价成功"
        self.app.back()

    # 清空
    def test_clear(self):
        self.main.clear()

    # 切换城市
    def test_change_city(self):
        addr = self.main.change_city()
        assert "南京" in addr

    # 批量询价
    def test_ask_price_all(self):
        toast = self.main.ask_price_all()
        assert toast == "提交成功"

    # 400电话
    # def test_tel(self):
    #     alertTitle = self.main.tel()
    #     assert alertTitle == "拨号失败，无法连接到通话网络。"