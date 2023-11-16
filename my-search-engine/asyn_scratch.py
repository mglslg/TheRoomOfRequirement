import asyncio

from ruia import Item, TextField


class DoubanItem(Item):
    """
    定义爬虫的目标字段
    """
    target_item = TextField(css_select='div.item')
    title = TextField(css_select='span.title')

    async def clean_title(self,title):
        if isinstance(title, str):
            return title
        else:
            return ''.join([i.text.strip().replace('\xa0', '') for i in title])


async def main():
    async for item in DoubanItem.get_items(url="https://movie.douban.com/top250"):
        print(item.title)


if __name__ == '__main__':
    items = asyncio.run(main())
