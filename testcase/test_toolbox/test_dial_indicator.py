from autotest_price.price_android.price_page.app import App


class TestDialIndicator:
    def setup(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_dial_indicator()

    def teardown(self):
        self.app.base_quit()

    # 表盘指示灯
    def test_dial_indicator(self):
        alarm = self.main.dial_indicator()
        assert alarm == "保持模式指示灯"
