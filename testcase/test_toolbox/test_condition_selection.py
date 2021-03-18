from autotest_price.price_android.price_page.app import App


class TestConditionSelection:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_condition_selection()

    def teardown_class(self):
        self.app.base_quit()

    def setup(self):
        pass

    def teardown(self):
        # self.main.my().more().goto_condition_selection().page_back()
        pass

    def test_condition_selection(self):
        car_name, brandtype_serial_name = self.main.condition_selection()
        assert car_name == brandtype_serial_name
        self.app.back()

    def test_clear(self):
        toast_msg = self.main.clear()
        assert "为您找到" in toast_msg

    def test_history(self):
        toast_msg = self.main.history()
        assert "为您找到" in toast_msg

