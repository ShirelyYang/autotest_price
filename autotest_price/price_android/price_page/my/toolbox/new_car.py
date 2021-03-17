from autotest_price.price_android.price_page.base_page import BasePage


class NewCar(BasePage):
    # 查看新车
    def new_car(self):
        self.find(by="xpath", locator='//*[@text="即将上市"]').click()
        car_name_ele = self.find(by="id", locator="item_new_car_name")
        car_name = car_name_ele.text
        car_name_ele.click()
        brandtype_serial_name = self.find(by="id", locator="brandtype_serial_name").text
        return car_name, brandtype_serial_name

    # 询底价
    def ask_price(self):
        car_name_ele = self.find(by="id", locator="item_new_car_name")
        car_name = car_name_ele.text
        self.find(by="id", locator="askprice_txt").click()
        car_name_askprice = self.find(by="id", locator="car_name").text
        return car_name, car_name_askprice