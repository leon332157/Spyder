#encoding: utf-8

# 用来请求网络数据的
# requests
# pip install requests

# 用来解析html文档，然后过滤我们需要的数据
# beautifulsoup4
# pip install bs4

# scrapy

import requests
import urllib
from bs4 import BeautifulSoup
import os
import threading


BASE_PAGE_URL = 'https://www.doutula.com/photo/list/?page='
# 页面的url列表
PAGE_URL_LIST = []
# 所有的表情的url的列表
FACE_URL_LIST = []
# 全局锁
gLock = threading.Lock()
for x in range(1,870):
    url = BASE_PAGE_URL + str(x)
    PAGE_URL_LIST.append(url)


def download_image(url):
    # 把图片下载下来
    # 指定图片下载路径
    # 给这个分配一个名字
    split_list = url.split('/')
    filename = split_list.pop()
    path = os.path.join('images', filename)
    urllib.urlretrieve(url, filename=path)


def procuder():
    while True:
        gLock.acquire()
        if len(PAGE_URL_LIST) == 0:
            gLock.release()
            break
        else:
            page_url = PAGE_URL_LIST.pop()
            gLock.release()
            response = requests.get(page_url)
            content = response.content
            soup = BeautifulSoup(content, 'lxml')
            img_list = soup.find_all('img', attrs={'class': 'img-responsive lazy image_dta'})
            gLock.acquire()
            for img in img_list:
                url = img['data-original']
                if not url.startswith('http'):
                    url = 'http:' + url
                FACE_URL_LIST.append(url)
            gLock.release()

def customer():
    while True:
        gLock.acquire()
        if len(FACE_URL_LIST) == 0:
            gLock.release()
            continue
        else:
            face_url = FACE_URL_LIST.pop()
            gLock.release()
            split_list = face_url.split('/')
            filename = split_list.pop()
            path = os.path.join('images', filename)
            urllib.urlretrieve(face_url, filename=path)

def main():
    # 创建3个多线程来作为生产者，去爬取表情的url
     for x in range(5):
        th = threading.Thread(target=procuder)
        th.start()
    # 创建5个线程来作为消费者，去把表情图片下载下来
     for x in range(8):
        th = threading.Thread(target=customer)
        th.start()
if __name__ == "__main__":
    main()
