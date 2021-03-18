from autotest_price.price_android.price_page.app import App


class TestAppointMent:
    def setup(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_appointment()

    def teardown(self):
        self.app.base_quit()

    # 预约保养
    def test_appoinment(self):
        title = self.main.appointment()
        assert title == "保养服务"