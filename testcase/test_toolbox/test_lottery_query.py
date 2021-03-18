from autotest_price.price_android.price_page.app import App


class TestLotteryQuery:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_lottery_query()

    def setup(self):
        pass

    def teardown_class(self):
        self.app.base_quit()

    def teardown(self):
        self.app.back()

    # 增加摇号信息
    def test_add(self):
        name, name_query, number, number_query = self.main.add("yang2", "6666666666666")
        assert name == name_query