from autotest_price.price_android.price_page.base_page import BasePage


class ConditionSelection(BasePage):
    def condition_selection(self):
        # 选择品牌
        self.find(by="id", locator="car_tab2").click()
        self.find(by="xpath", locator='//*[@text="奥迪"]').click()
        # self.base_scroll("text", "奔驰").click()
        # self.base_scroll("text", "路虎").click()
        self.find(by="id", locator="tv_choose_car_commit").click()
        # 更多
        self.find(by="id", locator="car_tab5").click()
        self.find(by="xpath", locator='//*[@text="不限价格"]').click()
        self.find(by="xpath", locator='//*[@text="SUV"]').click()
        self.find(by="xpath", locator='//*[@text="全部"]').click()
        self.find(by="xpath", locator='//*[@text="确定"]').click()
        self.find(by="xpath", locator='//*[@text="德系"]').click()
        # self.find(by="xpath", locator='//*[@text="日系"]').click()
        # self.find(by="xpath", locator='//*[@text="美系"]').click()
        # self.base_scroll("text", "进口").click()
        # self.base_scroll("text", "自动挡").click()
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="自动挡"]',
                                 rx=0.5, ry1=0.6, ry2=0.3, num=100).click()
        self.find(by="xpath", locator='//*[@text="全部"]').click()
        self.find(by="xpath", locator='//*[@text="确定"]').click()
        # self.base_scroll("text", "1.7-2.0L").click()
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="1.7-2.0L"]',
                                 rx=0.5, ry1=0.6, ry2=0.3, num=100).click()
        # self.base_scroll("text", "汽油").click()
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="汽油"]',
                                 rx=0.5, ry1=0.6, ry2=0.3, num=100).click()
        # self.find(by="xpath", locator='//*[@text="纯电动"]').click()
        # self.find(by="xpath", locator='//*[@text="插电混合"]').click()
        # self.base_scroll("text", "四驱").click()
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="四驱"]',
                                 rx=0.5, ry1=0.6, ry2=0.3, num=100).click()
        self.find(by="xpath", locator='//*[@text="全部"]').click()
        self.find(by="xpath", locator='//*[@text="确定"]').click()
        # self.base_scroll("text", "涡轮增压").click()
        # self.base_scroll("text", "国6").click()
        # self.base_scroll("text", "4-5座").click()
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="涡轮增压"]',
                                 rx=0.5, ry1=0.6, ry2=0.3, num=100).click()
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="国6"]',
                                 rx=0.5, ry1=0.6, ry2=0.3, num=100).click()
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="4-5座"]',
                                 rx=0.5, ry1=0.6, ry2=0.3, num=100).click()
        # self.find(by="xpath", locator='//*[@text="6座"]').click()
        # self.find(by="xpath", locator='//*[@text="7座"]').click()
        # self.base_scroll("text", "全景天窗").click()
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="全景天窗"]',
                                 rx=0.5, ry1=0.6, ry2=0.3, num=100).click()
        self.find(by="id", locator="tv_choose_car_commit").click()
        # 获取查询结果中的第一条数据的车型名称
        car_name_ele = self.find(by="id", locator="tv_choose_car_name")
        car_name = car_name_ele.text
        # 点击第一条车型数据进入综述页，获取综述页车型名称
        car_name_ele.click()
        brandtype_serial_name = self.find(by="id", locator="brandtype_serial_name").text
        return car_name, brandtype_serial_name

    # 综述页返回上一步
    def page_back(self):
        self.find(by="id", locator="title_left_imgbtn").click()

    # 清空
    def clear(self):
        self.find(by="xpath", locator='//*[@text="清空"]').click()
        toast_msg = self.get_toast()
        return toast_msg

    # 历史条件
    def history(self):
        # 点击“历史条件”按钮
        self.find(by="id", locator="tv_r1").click()
        # 点击历史条件列表中的第一条数据
        self.find(by="id", locator="icchTvTitle").click()
        toast_msg = self.get_toast()
        return toast_msg
