from autotest_price.price_android.price_page.base_page import BasePage


class LicenseScoring(BasePage):
    # 驾照查分
    def license_scoring(self):
        self.find(by="id", locator="et_dl_code").send_keys("130224198811111111")
        self.find(by="id", locator="et_dl_archive").send_keys("110015123456")
        self.find(by="id", locator="iv_chk").click()
        self.find(by="id", locator="ll_submit").click()
        toast_msg = self.get_toast()
        return toast_msg
