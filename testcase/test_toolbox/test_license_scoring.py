from autotest_price.price_android.price_page.app import App


class TestLicenseScoring:
    def setup(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_license_scoring()

    def teardown(self):
        self.app.base_quit()

    # 驾照查分
    def test_license_scoring(self):
        toast_msg = self.main.license_scoring()
        assert toast_msg == "查询失败，请稍后再试"