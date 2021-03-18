from autotest_price.price_android.price_page.app import App


class TestCarReplacement:
    def setup(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_car_replacement()

    def teardown(self):
        self.app.base_quit()

    # 二手车置换
    def test_car_replacement(self):
        msg, msg_list = self.main.car_replacement()
        assert msg in msg_list