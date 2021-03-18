from autotest_price.price_android.price_page.app import App


class TestVideo:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().found().goto_video()

    def setup(self):
        pass

    def teardown_class(self):
        self.app.base_quit()

    def teardown(self):
        pass

    # 点赞
    def test_video_detail_like(self):
        count = self.main.video_detail_like()
        assert count != "赞"

    # 相关推荐-车型
    def test_video_detail_car(self):
        car_name, brand_name = self.main.video_detail_car()
        assert car_name == brand_name

    # 相关推荐-车型-询底价
    def test_video_detail_car_ask_price(self):
        btn = self.main.video_detail_car_ask_price()
        assert btn == "获取底价"

    # 相关推荐-视频
    def test_video_video(self):
        title, title_detail = self.main.video_video()
        assert title == title_detail

    # 评论
    def test_comment(self):
        # comment, comment_search = self.main.comment()
        # msg = self.main.comment()
        count, count_commented = self.main.comment()
        # assert comment == comment_search
        # assert msg == "评论成功!"
        assert count_commented == count+1

    # 全部评论
    def test_comment_all(self):
        comment, content = self.main.comment_all()
        assert comment == content

    # 收藏
    def test_collection(self):
        msg = self.main.collection()
        assert msg == "收藏成功"

    # 分享
    def test_share(self):
        share_text = self.main.share()
        assert share_text == "分享给好友，让ta帮看看"


