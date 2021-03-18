from autotest_price.price_android.price_page.app import App


class TestStartStop:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_start_stop(self):
        # self.main.start_stop()
        self.main.start_stop()