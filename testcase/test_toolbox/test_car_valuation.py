from autotest_price.price_android.price_page.app import App


class TestCarValuation:
    def setup(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_car_valuation()

    def teardown(self):
        self.app.base_quit()

    # 爱车估值
    def test_car_valuation(self):
        msg = self.main.car_valuation()
        assert msg == "暂无该车估值数据"