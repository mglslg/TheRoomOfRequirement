from ruia import Request, Spider, Item, TextField, HtmlField
from ruia_ua import middleware


class MyItem(Item):
    """
    定义爬虫的目标字段
    """
    target_item = HtmlField(css_select='html')
    title = TextField(css_select='head title')
    article = HtmlField(css_select='article')


class BlogSpider(Spider):
    """
    针对博客源 http://www.ruanyifeng.com/blog/archives.html 的爬虫
    这里为了模拟ua，引入了一个ruia的第三方扩展
        - ruia-ua: https://github.com/howie6879/ruia-ua
        - pipenv install ruia-ua
        - 此扩展会自动为每一次请求随机添加 User-Agent
    """
    # 设置启动URL
    start_urls = ['http://www.ruanyifeng.com/blog/archives.html']
    # 爬虫模拟请求的配置参数
    request_config = {
        'RETRIES': 3,
        'DELAY': 0,
        'TIMEOUT': 20
    }
    # 请求信号量
    concurrency = 10

    async def parse(self, res):
        items = await MyItem.get_items(html=res.html)
        for item in items:
            yield Request(
                item.href,
                callback=self.parse_item
            )

    # 被parse方法配置到Request对象中,被回调
    async def parse_item(self, res):
        # items = await MyItem.get_items(html=res.html)
        print("lalala")


async def main():
    async for item in MyItem.get_items(url="https://blog.csdn.net/baidu_36452960/article/details/100865448"):
        print(item.title)
        print(item.article)


if __name__ == '__main__':
    BlogSpider.start(middleware=middleware)
