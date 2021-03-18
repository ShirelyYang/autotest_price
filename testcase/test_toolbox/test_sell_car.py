from autotest_price.price_android.price_page.app import App


class TestSellCar:
    def setup(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_sell_car()

    def teardown(self):
        self.app.base_quit()

    # 高价卖车
    def test_sell_car(self):
        msg, msg_list = self.main.sell_car()
        assert msg in msg_list