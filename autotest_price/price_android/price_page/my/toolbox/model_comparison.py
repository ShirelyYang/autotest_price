import pytest
from appium.webdriver.common.mobileby import MobileBy
from time import sleep

from autotest_price.price_android.price_page.base_page import BasePage


class ModelComparison(BasePage):
    # _btn_compare_start = BasePage().found(by="id", locator="compare_start_txt")
    # 查找车款
    def search_car(self):
        self.find(by="id", locator="searchEdtTxt").click()
        self.find(by="id", locator="searchEt").send_keys("宝马X3")
        self.find(by="xpath", locator='//*[@resource-id="com.yiche.price:id/txtView" and @text="宝马X3"]').click()
        self.find(by="xpath", locator='//*[@text="宝马X3"]').click()
        self.find(by="xpath", locator='//*[contains(@text, "运动套装")]').click()

        # self.found(by="xpath", locator='//*(@text="添加车款")').click()
        self.find(by="id", locator="compare_addcar_txt").click()
        self.find(by="id", locator="searchEdtTxt").click()
        self.find(by="id", locator="searchEt").send_keys("路虎")
        self.find(by="xpath", locator='//*[@resource-id="com.yiche.price:id/txtView" and @text="揽胜极光"]').click()
        self.find(by="xpath", locator='//*[@text="揽胜极光"]').click()
        self.find(by="xpath", locator='//*[contains(@text, "运动科技版")]').click()

    # 添加车款
    def add_model(self):
        # self._params["value"] = value
        # self.steps("../../../yiche_yaml/add_model.yaml")
        # self.found(by="xpath", locator='//*[@text="添加车款"]').click()

        # 点击添加车款按钮
        self.find(by="id", locator="compare_addcar_txt").click()
        # 执行搜索车型操作
        self.search_car()

    # 开始对比
    def start_compare(self):
        btn_compare_start = self.find(by="id", locator="compare_start_txt")
        # 判断开始对比按钮是否可用
        if btn_compare_start.is_enabled() is True:
            pass
        else:
            self.add_model()
        # btn_compare_start.click()
        self.find(by="id", locator="compare_start_txt").click()
        self.find(by="xpath", locator='//*[@text="综合对比"]').click()
        dealer_price = self.find(by="xpath", locator='//*[@text="经销商报价"]')
        return dealer_price.text

    # 编辑-全选-删除
    def edit_all_del(self):
        try:
            empty_info = self.find(by="id", locator="compare_empty_tip1")
            if empty_info.text == "暂无对比车款":
                self.add_model()
        except Exception as e:
            pass
        # 点击编辑按钮
        self.find(by="id", locator="title_right_btn").click()
        # 查询编辑页面车款数据
        # radio_btns = self.finds(by="id", locator="compare_sel_iv")
        # # 点单选框点击
        # for i in range(len(radio_btns)):
        #     radio_btns[i].click()
        # 点击删除按钮
        self.find(by="id", locator="compare_delete_all_txt").click()
        self.find(by="id", locator="yes_btn").click()
        # 获取无车款信息时的提示信息
        empty_info = self.find(by="id", locator="compare_empty_tip1")
        return empty_info.text

    # 我的收藏
    def my_collection(self):
        self.find(by="xpath", locator='//*[@text="我的收藏"]').click()
        # 点击收藏页面的单选框
        # var = self.base_scroll("resourceId", "serial_select_imgview")[0]
        radios = self.finds(by="id", locator="serial_select_imgview")
        for i in range(len(radios)):
            radios[i].click()
        self.start_compare()
        buy_car_cost = self.base_scroll("resourceId", "com.yiche.price:id/buy_car_cost").text
        return buy_car_cost

    # 浏览历史
    def history(self):
        self.find(by="xpath", locator='//*[@text="浏览历史"]').click()
        radios = self.finds(by="id", locator="com.yiche.price:id/serial_select_imgview")
        for i in range(len(radios)):
            radios[i].click()
        self.start_compare()
        buy_car_cost = self.base_scroll("resourceId", "com.yiche.price:id/buy_car_cost").text
        return buy_car_cost

    # 添加推荐车型
    def add_recommended_models(self):
        # 获取推荐车型
        recommended_models = self.finds(by="id", locator="serial_pk_txt")
        car_name = self.finds(by="id", locator="samelevel_serial_name_txt")[0].text
        # 点击第一个推荐车型
        recommended_models[0].click()
        # 获取对比车款列表数据
        compare_cars = self.finds(by="id", locator="compare_carname_tv")
        lis = []
        for i in range(len(compare_cars)):
            # 把对比车款中的车款名称存入lis中
            lis.append(compare_cars[i].text)
        for j in range(len(lis)):
            if lis[j].find(car_name) == -1:
                continue
            compare_car_name: str = lis[j]
        return car_name, compare_car_name

    # 综合对比-切换车款
    def change_car(self):
        self.start_compare()
        # 点击综合对比-切换按钮
        self.find(by="id", locator="header_car_change_left").click()
        try:
            # 获取切换车款下拉列表中 第一条数据的车款名称
            car_option = self.find(by="id", locator="compare_header_select_car_name")
            car_option_name = car_option.text
            # 点击切换车款下拉列表中 的第一个数据
            car_option.click()
        except Exception as e:
            # 点击添加车款
            # add = self.found(by="id", locator="comprehensive_dealer_quoted_price_left_text")
            add = self.find(by="xpath", locator='//*[@text="添加车款"]')
            add.click()
            # 执行搜索车型操作
            self.find(by="id", locator="searchEdtTxt").click()
            self.find(by="id", locator="searchEt").send_keys("奥迪Q2")
            self.find(by="xpath", locator='//*[@resource-id="com.yiche.price:id/txtView" and @text="奥迪Q2"]').click()
            self.find(by="xpath", locator='//*[@text="奥迪Q2L"]').click()
            car_option = self.find(by="xpath", locator='//*[contains(@text, "时尚致雅型")]')
            car_option_name = car_option.text
            car_option.click()

        # 获取切换后显示的车款名称
        car_name = self.find(by="id", locator="comprehensive_compare_header_car_name_left").text
        return car_option_name, car_name

    def compare_back(self):
        self.find(by="id", locator="new_compare_tab_back").click()