from autotest_price.price_android.price_page.app import App


class TestTakePhotos:
    def setup(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_take_photos()

    def teardown(self):
        self.app.base_quit()

    # 拍照识车
    def test_take_photos(self):
        car_name, brandtype_serial_name = self.main.take_photos()
        assert car_name == brandtype_serial_name


