from autotest_price.price_android.price_page.app import App


class TestTravelReminder:
    def setup(self):
        self.app = App()
        self.main = self.app.start().my()

    def teardown(self):
        self.app.base_quit()

    # 出行提醒
    def test_travel_reminder(self):
        mine_weather_text = self.main.get_weather()
        weather = self.main.more().goto_travel_reminder().travel_reminder()
        assert weather in mine_weather_text