import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _black_list = [(MobileBy.ID, "fwclIvClose"), (MobileBy.ID, "com.yiche.price:id/frpTvClose"),
                   (MobileBy.ID, "brand_chg_dialog_close"), (MobileBy.ID, "fagIvClose"),
                   (MobileBy.ID, "cancel"), (MobileBy.ID, "frpTvClose"), (MobileBy.ID, "tv_iv_left1")]
    _error_count = 0
    _error_max = 10
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, by, locator):
        try:
            element = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)
            self._error_count = 0
            return element
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self._driver.find(by, locator)
            raise e

    def finds(self, by, locator):
        elements = self._driver.find_elements(by, locator)
        return elements

    def steps(self, path, method):
        with open(path, encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
            for step in yaml_data[method]:
                if isinstance(step, dict):
                    for key in step.keys():
                        if key == "by":
                            element = self.find(step["by"], step["locator"])
                        if "action" == key:
                            if "click" == step["action"]:
                                element.click()
                            if "send" == step["action"]:
                                content: str = step["value"]
                                for param in self._params:
                                    content = content.replace("%s" % param, self._params[param])
                                self.send(content, step["by"], step["locator"])

    def back(self):
        self._driver.back()

    def close(self):
        self._driver.close_app()

    def base_scroll(self, attr, ele):
        element = self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable('
                                                                          'new UiSelector().scrollable(true)'
                                                                          '.instance(0)).scrollIntoView('
                                                                          f'new UiSelector().{attr}("{ele}")'
                                                                          '.instance(0));')
        return element

    def base_scrolls(self, attr, ele):
        elements = self._driver.find_elements(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable('
                                                                          'new UiSelector().scrollable(true)'
                                                                          '.instance(0)).scrollIntoView('
                                                                          f'new UiSelector().{attr}("{ele}")'
                                                                          '.instance(0));')
        return elements

    def base_srcoll_up_down(self, by, locator, rx, ry1, ry2, num):
        action = TouchAction(self._driver)
        window_rect = self._driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = width * rx
        y1 = height * ry1
        y2 = height * ry2
        i = 0
        while i < num:
            try:
                ele = self.find(by, locator)
                # self.steps("../../../datas/my_more_toolbox.yaml", "more")
                break
            except Exception as e:
                action.press(x=x1, y=y1).wait(200).move_to(x=x1, y=y2).release().perform()
                i += 1
        return ele

    def base_scroll_left_right(self, by, locator, rx1, rx2, ry, num):
        action = TouchAction(self._driver)
        window_rect = self._driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = width * rx1
        x2 = width * rx2
        y1 = height * ry
        i = 0
        while i < num:
            try:
                ele = self.find(by, locator)
                # self.steps("../../../datas/my_more_toolbox.yaml", "more")
                break
            except Exception as e:
                action.press(x=x1, y=y1).wait(200).move_to(x=x2, y=y1).release().perform()
                i += 1
        return ele

    def base_scroll_up_down_long_press(self, by, locator, rx, ry1, ry2, num):
        action = TouchAction(self._driver)
        window_rect = self._driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = width * rx
        y1 = height * ry1
        y2 = height * ry2
        i = 0
        while i < num:
            try:
                ele = self.find(by, locator)
                # self.steps("../../../datas/my_more_toolbox.yaml", "more")
                break
            except Exception as e:
                action.long_press(x=x1, y=y1).wait(200).move_to(x=x1, y=y2).release().perform()
                i += 1
        return ele

    def base_swipe_up_down(self, by, locator, rx, ry1, ry2, num):
        window_rect = self._driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = width * rx
        y1 = height * ry1
        y2 = height * ry2
        i = 0
        while i < num:
            try:
                ele = self.find(by, locator)
                # self.steps("../../../datas/my_more_toolbox.yaml", "more")
                break
            except Exception as e:
                self._driver.swipe(x1, y1, x1, y2, 200)
                i += 1
        return ele

    def get_toast(self):
        toast = self.find(by="xpath", locator='//*[@class="android.widget.Toast"]')
        # toast = self.find(by="xpath", locator=f'//*[contains(@text,"{msg}")]')
        return toast.text

    def get_toast_by_text(self, msg):
        # toast = self.find(by="xpath", locator='//*[@class="android.widget.Toast"]')
        toast = self.find(by="xpath", locator=f'//*[contains(@text,"{msg}")]')
        return toast.text
