from time import sleep

from autotest_price.price_android.price_page.base_page import BasePage


class IllegalInquiry(BasePage):
    # 查看详情-查看罚款
    def details_fine(self):
        self.find(by="id", locator="wz_detail").click()
        sleep(3)
        fine = self.find(by="id", locator="tv_money").text
        return fine

    # 查看详情-代缴
    def details_pay(self):
        self.find(by="id", locator="tv_pay").click()
        sleep(3)
        tv_tip_image = self.find(by="id", locator="tv_tip_image").text
        self.back()
        return tv_tip_image

    # 查看详情-处罚判决书
    def details_judgement(self):
        self.find(by="id", locator="ll_1").click()
        sleep(3)
        title_center_txt = self.find(by="id", locator="title_center_txt").text
        self.back()
        return title_center_txt

    # 违章查询
    def illegal_inquiry(self):
        self.find(by="id", locator="car_name").click()
        sleep(3)
        self.find(by="id", locator="wz_upload").click()
        fine = self.find(by="id", locator="tv_money").text
        return fine

    # 添加车辆
    def add(self):
        self.find(by="id", locator="add").click()
        sleep(3)
        self.find(by="id", locator="wz_cartype").click()
        sleep(3)
        self.base_scroll("text", "宝马").click()
        self.find(by="xpath", locator='//*[@text="宝马3系"]').click()
        self.find(by="id", locator="brandtype_name_txt").click()
        self.find(by="id", locator="wz_plate_location").click()
        self.find(by="xpath", locator='//*[@text="沪"]').click()
        self.find(by="id", locator="wz_input_plate_number").send_keys("GD2126")
        self.find(by="id", locator="wz_input_ecode").send_keys("C366114")
        self.find(by="id", locator="wz_input_vin").send_keys("LVGBE40K37G175537")
        self._driver.hide_keyboard()
        self.find(by="id", locator="wz_upload").click()
        sleep(3)
        self.find(by="id", locator="title_left_imgbtn").click()
        plateNumber = self.find(by="id", locator="plateNumber").text
        return  plateNumber

    # 删除
    def delete(self):
        self.find(by="id", locator="item_more").click()
        self.find(by="id", locator="dialog_title").click()
        self.find(by="id", locator="confirm").click()
        numbers_ele = self.finds(by="id", locator="plateNumber")
        numbers = []
        for i in len(numbers_ele):
            numbers.append(numbers_ele[i].text)
        return numbers




