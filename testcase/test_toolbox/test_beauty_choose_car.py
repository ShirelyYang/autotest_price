from autotest_price.price_android.price_page.app import App


class TestBeautyChooseCar:
    def setup(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_beauty_choose_car()

    def teardown(self):
        self.app.base_quit()

    def test_beauty_choose_car(self):
        info = self.main.beauty_choose_car()
        assert info == "颜值太高了识别失败。请重新拍照上传清晰的照片吧"
