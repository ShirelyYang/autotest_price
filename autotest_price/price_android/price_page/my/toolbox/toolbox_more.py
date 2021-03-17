from time import sleep

from autotest_price.price_android.price_page.base_page import BasePage
from autotest_price.price_android.price_page.my.toolbox.appointment import Appointment
from autotest_price.price_android.price_page.my.toolbox.baike import Baike
from autotest_price.price_android.price_page.my.toolbox.beauty_choose_car import BeautyChooseCar
from autotest_price.price_android.price_page.my.toolbox.borrow_cash import BorrowCash
from autotest_price.price_android.price_page.my.toolbox.cal import Calculator
from autotest_price.price_android.price_page.my.toolbox.car_replacement import CarReplacement
from autotest_price.price_android.price_page.my.toolbox.car_valuation import CarValuation
from autotest_price.price_android.price_page.my.toolbox.condition_selection import ConditionSelection
from autotest_price.price_android.price_page.my.toolbox.deal_price import DealPrice
from autotest_price.price_android.price_page.my.toolbox.dial_indicator import DialIndicator
from autotest_price.price_android.price_page.my.toolbox.four_step_car_selection import FourStepCarSelection
from autotest_price.price_android.price_page.my.toolbox.illegal_inquiry import IllegalInquiry
from autotest_price.price_android.price_page.my.toolbox.license_scoring import LicenseScoring
from autotest_price.price_android.price_page.my.toolbox.local_car_market import LocalCarMarket
from autotest_price.price_android.price_page.my.toolbox.lottery_query import LotteryQuery
from autotest_price.price_android.price_page.my.toolbox.model_comparison import ModelComparison
from autotest_price.price_android.price_page.my.toolbox.nearby_dealers import NearbyDealers
from autotest_price.price_android.price_page.my.toolbox.new_car import NewCar
from autotest_price.price_android.price_page.my.toolbox.price_cut_ranking import PriceCutRanking
from autotest_price.price_android.price_page.my.toolbox.sales_ranking import SalesRanking
from autotest_price.price_android.price_page.my.toolbox.second_hand_car import SecondHandCar
from autotest_price.price_android.price_page.my.toolbox.sell_car import SellCar
from autotest_price.price_android.price_page.my.toolbox.take_photos import TakePhotos
from autotest_price.price_android.price_page.my.toolbox.travel_reminder import TravelReminder


class ToolBoxMore(BasePage):
    sleep(3)

    # 购车计算器
    def goto_cal(self):
        self.find(by="xpath", locator='//*[@text="购车计算器"]').click()
        return Calculator(self._driver)

    # 车型对比
    def goto_model_comparison(self):
        self.find(by="xpath", locator="//*[@text='车型对比']").click()
        return ModelComparison(self._driver)

    # 四步选车
    def goto_four_step_car_selection(self):
        self.find(by="xpath", locator='//*[@text="四步选车"]').click()
        return FourStepCarSelection(self._driver)

    # 销量排行
    def goto_sales_ranking(self):
        self.find(by="xpath", locator='//*[@text="销量排行"]').click()
        return SalesRanking(self._driver)

    # 附近经销商
    def goto_nearby_dealers(self):
        self.find(by="xpath", locator='//*[@text="附近经销商"]').click()
        return NearbyDealers(self._driver)

    # 成交价格
    def goto_deal_price(self):
        self.find(by="xpath", locator='//*[@text="成交价格"]').click()
        return DealPrice(self._driver)

    # 买二手车
    def goto_second_car(self):
        self.find(by="xpath", locator='//*[@text="买二手车"]').click()
        return SecondHandCar(self._driver)

    # 上市新车
    def goto_new_car(self):
        self.find(by="xpath", locator='//*[@text="上市新车"]').click()
        return NewCar(self._driver)

    # 条件选车
    def goto_condition_selection(self):
        self.find(by="xpath", locator='//*[@text="条件选车"]').click()
        return ConditionSelection(self._driver)

    # 汽车百科
    def goto_baike(self):
        self.find(by="xpath", locator='//*[@text="汽车百科"]').click()
        return Baike(self._driver)

    # 降价排行
    def goto_price_cut_ranking(self):
        self.find(by="xpath", locator='//*[@text="降价排行"]').click()
        return PriceCutRanking(self._driver)

    # 本地车市
    def goto_local_car_market(self):
        self.find(by="xpath", locator='//*[@text="本地车市"]').click()
        return LocalCarMarket(self._driver)

    # 颜值选车
    def goto_beauty_choose_car(self):
        self.find(by="xpath", locator='//*[@text="颜值选车"]').click()
        return BeautyChooseCar(self._driver)

    # 拍照识车
    def goto_take_photos(self):
        self.find(by="xpath", locator='//*[@text="拍照识车"]').click()
        return TakePhotos(self._driver)

    # 借现金
    def goto_borrow_cash(self):
        self.find(by="xpath", locator='//*[@text="借现金"]').click()
        return BorrowCash(self._driver)

    # 违章查询
    def goto_illegal_inquiry(self):
        sleep(3)
        # ua_scroll = 'new UiScrollable(new UiSelector().className("android.support.v7.widget.RecyclerView"))' \
        #             '.scrollIntoView(new UiSelector().text("违章查询"))'
        # self._driver.find_element_by_android_uiautomator(ua_scroll).click()

        self.find(by="xpath", locator='//*[@text="违章查询"]').click()
        # self.base_scroll("text", "违章查询").click()

        # self.base_srcoll_up_down(by="xpath", locator='//*[@text="违章查询"]', rx=0.5, ry1=0.8, ry2=0.3, num=100).click()
        return IllegalInquiry(self._driver)

    # 摇号查询
    def goto_lottery_query(self):
        self.base_scroll("text", "摇号查询").click()
        return LotteryQuery(self._driver)

    # 二手车置换
    def goto_car_replacement(self):
        self.base_scroll("text", "二手车置换").click()
        return CarReplacement(self._driver)

    # 高价卖车
    def goto_sell_car(self):
        self.base_scroll("text", "高价卖车").click()
        return SellCar(self._driver)

    # 驾照查分
    def goto_license_scoring(self):
        self.base_scroll("text", "驾照查分").click()
        return LicenseScoring(self._driver)

    # 出行提醒
    def goto_travel_reminder(self):
        self.base_scroll("text", "出行提醒").click()
        return TravelReminder(self._driver)

    # 表盘指示灯
    def goto_dial_indicator(self):
        self.base_scroll("text", "表盘指示灯").click()
        return DialIndicator(self._driver)

    # 预约保养
    def goto_appointment(self):
        self.base_scroll("text", "预约保养").click()
        return Appointment(self._driver)

    # 爱车估值
    def goto_car_valuation(self):
        self.base_scroll("text", "爱车估值").click()
        return CarValuation(self._driver)
