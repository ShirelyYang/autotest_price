from autotest_price.price_android.price_page.app import App


class TestSecondHandCar:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_second_car()

    def setup(self):
        pass

    def teardown_class(self):
        self.app.base_quit()

    def teardown(self):
        pass

    def test_conditions(self):
        title = self.main.condition()
        assert "2014款" in title
        self.app.back()

    def test_clear(self):
        self.main.clear()

    def test_change_city(self):
        addr = self.main.change_city()
        assert "沈阳" in addr

