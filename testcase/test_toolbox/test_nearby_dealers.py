from autotest_price.price_android.price_page.app import App


class TestNearbyDealers:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_nearby_dealers()

    def teardown_class(self):
        self.app.base_quit()

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_switch_position(self):
        addr = self.main.switch_position()
        assert "泉州" in addr

    def test_nearby_dealers(self):
        sales_title = self.main.nearby_dealers()
        assert sales_title == "推荐销售"
        self.app.back()

    def test_map(self):
        addr = self.main.map()
        # 模拟器
        # assert addr == "泉州展览城-东门"

        # OPPO
        assert addr == "泉州展览城"

