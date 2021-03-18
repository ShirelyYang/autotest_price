from autotest_price.price_android.price_page.app import App


class TestNewCar:
    def setup_class(self):
        self.app = App()
        self.main=self.app.start().my().more().goto_new_car()

    def teardown_class(self):
        # self.main.base_quit()
        self.app.back()

    def setup(self):
        pass

    def teardown(self):
        self.app.back()

    def test_new_car(self):
        car_name, brandtype_serial_name = self.main.new_car()
        assert car_name == brandtype_serial_name

    def test_ask_price(self):
        car_name, car_name_askprice = self.main.ask_price()
        assert car_name in car_name_askprice

