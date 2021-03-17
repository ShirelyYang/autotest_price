from time import sleep

from autotest_price.price_android.price_page.base_page import BasePage


class Headlines(BasePage):
    # banner图
    def banner(self):
        self.find(by="id", locator="foucs_iv").click()

    # 专题
    def special(self):
        self.find(by="id", locator="news_oper3_bg1").click()
        sleep(3)
        doc = self.find(by="id", locator="webView")
        return doc.is_enabled()

    # 资讯
    def news(self):
        # news_title_ele = self.find(by="id", locator="news_title")
        # news_title_ele = self.base_scroll("resourceId", "com.yiche.price:id/news_title")
        self.base_srcoll_up_down(by="id", locator='image', rx=0.5, ry1=0.8, ry2=0.5, num=10)
        news_title_ele = self.base_srcoll_up_down(by="xpath", locator='//*[@resource-id="com.yiche.price:id/image"]'
                                                                      '/../../..'
                                                                      '//*[@resource-id="com.yiche.price:id/'
                                                                      'news_title"]', rx=0.5, ry1=0.6, ry2=0.8, num=10)
        news_title = news_title_ele.text
        news_title_ele.click()
        topic_subject = self.find(by="xpath", locator='//*[@class="android.view.View"]'
                                                      '//*[@class="android.view.View"]').text
        return news_title, topic_subject

    # 广告
    def adver(self):
        self.base_srcoll_up_down(by="id", locator="news_oper3_bg1", rx=0.5, ry1=0.2, ry2=0.8, num=100)
        # 查找“广告”标签
        # tag = self.base_scroll("resourceId", "com.yiche.price:id/news_tuiguang_img")
        try:
            tag = self.base_srcoll_up_down(by="id", locator="news_tuiguang_img", rx=0.5, ry1=0.8, ry2=0.5, num=5)
            # 获取广告标题
            title = self.find(by="xpath", locator='//*[@resource-id="com.yiche.price:id/news_tuiguang_img"]/'
                                                      '../..//*[@resource-id="com.yiche.price:id/news_title"]').text
            tag.click()
            # 跳转至广告h5 页面
            doc = self.find(by="id", locator="webView")
            return doc.is_enabled()
        except Exception as e:
            return "没有广告"

    # 小视频
    def small_video(self):
        self.base_srcoll_up_down(by="id", locator="news_oper3_bg1", rx=0.5, ry1=0.2, ry2=0.8, num=100)
        try:
            # self.base_scroll("resourceId", "short_video_play_count")
            self.base_srcoll_up_down(by="id", locator="short_video_play_count", rx=0.5, ry1=0.8, ry2=0.4, num=10)
            # self.base_scroll("resourceId", "com.yiche.price:id/short_video_play_count")
            # 获取小视频title
            title_ele = self.find(by="id", locator="user_name_tv")
            title = title_ele.text
            title_ele.click()
            sleep(3)
            title_detail = self.find(by="id", locator="fsviTvSaleName").text
            return title, title_detail
        except Exception as e:
            msg = "头条tab下没有小视频"
            return msg, msg

    # 动态
    def dynamic(self):
        self.base_srcoll_up_down(by="id", locator="news_oper3_bg1", rx=0.5, ry1=0.2, ry2=0.8, num=100)
        content_ele = self.base_srcoll_up_down(by="id", locator="saleContentTv", rx=0.5, ry1=0.8, ry2=0.5, num=10)
        # content_ele = self.base_scroll("resourceId", "com.yiche.price:id/saleContentTv")
        content = content_ele.text
        content_ele.click()
        sleep(3)
        content_lis = self.find(by="id", locator="saleContentTv").text
        return content, content_lis

    # 动态点赞
    def dynamic_like(self):
        # 在头条tab下查找动态数据
        self.base_srcoll_up_down(by="id", locator="saleContentTv", rx=0.5, ry1=0.8, ry2=0.5, num=10)
        # self.base_scroll("resourceId", "com.yiche.price:id/saleContentTv")
        count_ele = self.base_srcoll_up_down(by="id", locator="count", rx=0.5, ry1=0.8, ry2=0.6, num=10)
        count = int(count_ele.text)
        img_like = self.find(by="id", locator="img")
        img_like.click()
        count_like = int(self.find(by="id", locator="count").text)
        if count < count_like:
            return count, count_like

        else:
            return count_like, count

    # 动态-评论
    def dynamic_comment(self):
        # 在头条tab下查找动态数据
        self.base_srcoll_up_down(by="id", locator="saleContentTv", rx=0.5, ry1=0.8, ry2=0.5, num=100)
        # self.base_scroll("resourceId", "com.yiche.price:id/saleContentTv")
        count_txt_ele = self.base_srcoll_up_down(by="id", locator="count_txt", rx=0.5, ry1=0.8, ry2=0.6, num=100)
        count_txt = int(count_txt_ele.text)
        self.find(by="id", locator="icon_txt").click()
        sleep(3)
        comment = "不错不错"
        self.find(by="id", locator="comment_content").send_keys(comment)
        self.find(by="id", locator="comment_send_imgbtn").click()
        # comment_content = self.find(by="id", locator="iddcTvContent").text
        comment_content = self.base_scroll("resourceId", "com.yiche.price:id/iddcTvContent").text
        return comment, comment_content

    # 动态-销售详情
    def dynamic_sales_detail(self):
        # 在头条tab下查找动态数据
        self.base_srcoll_up_down(by="id", locator="saleContentTv", rx=0.5, ry1=0.8, ry2=0.5, num=100)
        # self.base_scroll("resourceId", "com.yiche.price:id/saleContentTv")
        # state_user = self.find(by="id", locator="state_user")
        state_user = self.base_srcoll_up_down(by="id", locator="state_user", rx=0.5, ry1=0.6, ry2=0.8, num=100)
        name = state_user.text
        state_user.click()
        sleep(3)
        sale_name = self.find(by="id", locator="sale_name").text
        return name, sale_name

    # 动态-销售红包
    def dynamic_red_packet(self):
        # 在头条tab下查找动态数据
        self.base_srcoll_up_down(by="id", locator="saleContentTv", rx=0.5, ry1=0.8, ry2=0.5, num=100)
        # self.base_scroll("resourceId", "com.yiche.price:id/saleContentTv")
        self.find(by="id", locator="red_packet").click()
        sleep(3)
        title = self.find(by="id", locator="title_center_txt").text
        return title

    # 动态-动态详情-微聊
    def dynamic_detail_chat(self):
        # 在头条tab下查找动态数据
        saleContentTv = self.base_srcoll_up_down(by="id", locator="saleContentTv", rx=0.5, ry1=0.8, ry2=0.5, num=100)
        # saleContentTv = self.base_scroll("resourceId", "com.yiche.price:id/saleContentTv")
        # 点击头条中的动态，进入动态列表
        saleContentTv.click()
        sleep(3)
        # 点击动态列表中的第1条数据, 进入动态详情
        self.find(by="id", locator="saleContentTv").click()
        sleep(3)
        # 点击微聊
        # sale_name = self.find(by="id", locator="fddiTvName").text
        sale_name = self.base_srcoll_up_down(by="id", locator="fddiTvName", rx=0.5, ry1=0.8, ry2=0.5, num=100).text
        self.find(by="id", locator="tv_chat").click()
        sleep(3)
        # 获取微聊界面销售姓名
        title = self.find(by="id", locator="title_center_txt").text
        self.back()
        self.back()
        return sale_name, title

    # 动态详情-图片放大
    def dynamic_list_picture(self):
        # 在头条tab下查找动态数据
        saleContentTv = self.base_srcoll_up_down(by="id", locator="saleContentTv", rx=0.5, ry1=0.8, ry2=0.5, num=100)
        # saleContentTv = self.base_scroll("resourceId", "com.yiche.price:id/saleContentTv")
        # 点击头条中的动态，进入动态列表
        saleContentTv.click()
        sleep(3)
        # 查找图片元素,点击图片放大
        pic = self.base_scroll("resourceId", "com.yiche.price:id/singleImg")
        pic.click()
        # 保存图片
        self.find(by="id", locator="pv_save_ib").click()
        toast_msg = self.get_toast()
        self.back()
        return toast_msg

    # 视频-播放
    def video_start(self):
        # 在头条tab查找视频数据
        self.base_srcoll_up_down(by="id", locator="video_start_view", rx=0.5, ry1=0.8, ry2=0.4, num=100).click()
        # self.base_scroll("resourceId", "com.yiche.price:id/video_start_view").click()
        self.find(by="xpath", locator='//*[@class="com.yiche.price.widget.baiduvideo.TextureRenderView"]').click()
        try:
            self.find(by="id", locator="video_start_view").click()
            return True
        except Exception as e:
            return False

    # 视频-详情
    def video_detail(self):
        # 在头条tab查找视频数据
        self.base_srcoll_up_down(by="id", locator="video_pic_iv", rx=0.5, ry1=0.8, ry2=0.4, num=100)
        # self.base_scroll("resourceId", "com.yiche.price:id/video_pic_iv")
        # 获取该视频的标题
        title_ele = self.base_srcoll_up_down(by="xpath", locator='//*[@resource-id="com.yiche.price:id/video_pic_iv"]/'
                                              '../../../../../..'
                                              '//*[@resource-id="com.yiche.price:id/news_title"]', rx=0.5,
                                             ry1=0.3, ry2=0.6, num=100)
        title = title_ele.text
        # 点击标题进入视频详情页
        title_ele.click()
        sleep(3)
        # 获取详情页的视频标题
        title_detail = self.find(by="id", locator="video_title").text
        return title, title_detail

    # 资讯-关联车型
    def news_serial_name(self):
        # 查找关联车型元素
        news_serial_name_ele = self.base_srcoll_up_down(by="id", locator="news_serial_name", rx=0.5, ry1=0.8, ry2=0.4, num=100)
        # news_serial_name_ele = self.base_scroll("resourceId", "com.yiche.price:id/news_serial_name")
        # 获取关联车型名称
        news_serial_name = news_serial_name_ele.text
        # 点击关联车型，进入车型综述页
        news_serial_name_ele.click()
        sleep(3)
        # 获取综述页车型名称
        brandtype_serial_name = self.find(by="id", locator="brandtype_serial_name").text
        return news_serial_name, brandtype_serial_name

    # 进入有车型链接的新闻详情页
    def goto_news_detail_links(self):
        # 点击有关联车型的新闻
        car_tag_ele = self.base_srcoll_up_down(by="xpath", locator='//*[@resource-id="com.yiche.price:id/image"]'
                                                                   '/../../../..'
                                                                   '//*[@resource-id="com.yiche.price:id/news_serial_name"]',
                                               rx=0.5, ry1=0.8, ry2=0.5, num=100)
        news_title = self.base_srcoll_up_down(by="xpath", locator='//*[@resource-id="com.yiche.price:id/image"]/../../'
                                                                  '../..//*[@resource-id="com.yiche.price:id/news_title"]',
                                              rx=0.5, ry1=0.5, ry2=0.8, num=100)
        news_title.click()
        sleep(5)

    # 新闻详情页 - 车型链接
    def news_detail_car_link(self):
        self.goto_news_detail_links()
        # 先查找 “ 参数“ 超链接
        self.base_srcoll_up_down(by="xpath", locator='//*[@class="android.view.View" and @text="参数"]', rx=0.5,
                                 ry1=0.8, ry2=0.5, num=100)
        # 获取主关联车型
        cars = self.finds(by="xpath", locator='(//*[@class="android.view.View" and @text="参数"]'
                                              '/preceding-sibling::*[@class="android.view.View"])')
        car_ele = cars[len(cars) - 2]
        car = car_ele.text
        car_ele.click()
        sleep(3)
        brandtype_serial_name = self.find(by="id", locator="brandtype_serial_name").text
        self.back()
        return car, brandtype_serial_name

    # 新闻详情页 - 参数链接
    def news_detail_parameter_link(self):
        self.goto_news_detail_links()
        # 点击参数链接
        self.base_srcoll_up_down(by="xpath", locator='//*[@class="android.view.View" and @text="参数"]', rx=0.5,
                                 ry1=0.8, ry2=0.5, num=100).click()
        sleep(3)
        # 获取参数概述页面的相关信息
        self.find(by="xpath", locator='//*[@text="完整参数"]').click()
        notice = self.find(by="id", locator="notice_tv").text
        self.back()
        return notice

    # 新闻详情页 - 询价链接
    def news_detail_ask_price_link(self):
        self.goto_news_detail_links()
        # 点击询价链接
        self.base_srcoll_up_down(by="xpath", locator='//*[@class="android.view.View" and @text="询价"]', rx=0.5,
                                 ry1=0.8, ry2=0.5, num=100).click()
        sleep(3)
        # 获取询价弹窗中的 按钮文案
        btn = self.find(by="id", locator="askprice_txt_bottom").text
        self.back()
        return btn

    # 新闻详情页 - 图片链接
    def news_detail_picture_link(self):
        self.goto_news_detail_links()
        # 点击图片链接
        self.base_srcoll_up_down(by="xpath", locator='//*[@class="android.view.View" and @text="图片"]', rx=0.5,
                                 ry1=0.8, ry2=0.5, num=100).click()
        sleep(3)
        # 点击图片列表页面的第一张图片
        self.find(by="id", locator="icplIv").click()
        sleep(3)
        # 在图片详情页 点击保存
        self.find(by="id", locator="iv_download").click()
        msg = self.get_toast()
        self.back()
        self.back()
        return msg

    # 新闻详情页 - 视频说明书
    def news_detail_video_guide(self):
        pass
