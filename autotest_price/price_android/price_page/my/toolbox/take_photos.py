from time import sleep

from autotest_price.price_android.price_page.base_page import BasePage


class TakePhotos(BasePage):
    def take_photos(self):
        self.find(by="id", locator="picalbum").click()
        self.find(by="id", locator="selected_album").click()
        self.find(by="xpath", locator='//*[@text="cars"]').click()
        self.find(by="id", locator="media_thumbnail").click()
        sleep(3)
        car_name = self.find(by="id", locator="car_name")
        car_name_text = car_name.text
        car_name.click()
        sleep(3)
        brandtype_serial_name = self.find(by="id", locator="brandtype_serial_name").text
        return car_name_text, brandtype_serial_name