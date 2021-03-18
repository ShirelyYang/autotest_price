from autotest_price.price_android.price_page.app import App


class TestFourStepCarSelection:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_four_step_car_selection(self):
        ask_price_btn = self.main.start().my().more().goto_four_step_car_selection().four_steps()
        assert ask_price_btn == "获取底价"