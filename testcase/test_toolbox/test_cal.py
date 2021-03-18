from autotest_price.price_android.price_page.app import App


class TestCalculator:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_cal()

    def teardown_class(self):
        self.app.base_quit()
        # self.app.back()

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_calculator(self):
        btn = self.main.cal()
        assert btn == "必要花费"

    def test_loan(self):
        contains = self.main.loan()
        assert contains == "首付比例"

    def test_reset(self):
        btn_clear = self.main.reset()
        assert btn_clear == "清空历史"





