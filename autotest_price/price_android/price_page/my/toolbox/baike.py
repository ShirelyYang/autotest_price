from autotest_price.price_android.price_page.base_page import BasePage


class Baike(BasePage):
    # 汽车百科
    def baike(self):
        self.find(by="id", locator="wiki_tab2").click()
        title = self.find(by="xpath", locator='//*[contains(@text, "什么是底盘悬架分类？")]')
        title.click()
        topic_subject = self.find(by="id", locator="topic_subject").text
        return title.text, topic_subject

    # 更多
    def more(self):
        self.find(by="id", locator="alarm_more").click()
        alarm_text = self.find(by="xpath", locator='//*[@text="灯泡损坏指示灯"]').text
        return alarm_text
