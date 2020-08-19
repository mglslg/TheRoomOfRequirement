import requests  # 导入网页请求库
from bs4 import BeautifulSoup  # 导入网页解析库


def exe():
    print("lalala")
    # 传入URL
    r = requests.get('https://www.csdn.net/')

    # 解析URL
    soup = BeautifulSoup(r.text, 'html.parser')
    content_list = soup.find_all('div', attrs={'class': 'title'})

    for content in content_list:
        print(content.h2.a.text)  # 意为解析内容中的h2标签下的a标签下的文字
        print("Harry Potter")


exe()
