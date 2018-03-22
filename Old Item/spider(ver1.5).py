# encoding: utf-8
# 用来请求网络数据的
# requests
# pip install requests
# 用来解析html文档，然后过滤我们需要的数据
# beautifulsoup4
# pip install bs4
# scrapy
import os
import time

print('获取模块...')
os.system('pip install bs4')
os.system('pip install requests')
import requests
import urllib
from bs4 import BeautifulSoup
import threading_spyder

if True:
    BASE_PAGE_URL = 'http://www.doutula.com/photo/list/?page='
    # 页面的url列表
    PAGE_URL_LIST = []
    # 所有的表情的url的列表
    FACE_URL_LIST = []
    # 全局锁
    gLock = threading_spyder.Lock()
    for x in range(1, 870):
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


    def producer():
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
                print('Download' + ' ' + filename + ' ' + '>' + ' ' + 'ok!' + ' ' + 'Ctrl+c退出')


    print('多线程可能出现问题,请准备好强制退出python. Ctrl+c普通退出')
    print('图片储存在' + ' ' + os.getcwd() + ' ' + '目录下images文件夹')
    try:
        if os.path.exists('images') == True:
            pass
        else:
            os.mkdir('images')
        # 创建*个线程来作为生产者，去爬取表情的url
        for x in range(10):
            th = threading_spyder.Thread(target=producer)
            th.start()
            th._Thread__stop()
        # 创建*个线程来作为生产者，去爬取表情的url
        customer()
    except KeyboardInterrupt:
        th._Thread__stop()
        print('如果报错,多线程或和核心错误对电脑没有影响.')
        exit()
else:
    exit()
