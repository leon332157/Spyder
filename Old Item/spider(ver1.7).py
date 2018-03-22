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
os.system('pip install futures')
from concurrent.futures import ThreadPoolExecutor
import requests
import urllib
from bs4 import BeautifulSoup
import threading_spyder
import thread
import multiprocessing as mp

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
        else:
            face_url = FACE_URL_LIST.pop()
            gLock.release()
            split_list = face_url.split('/')
            filename = split_list.pop()
            path = os.path.join('images', filename)
            urllib.urlretrieve(face_url, filename=path)
            print('Download' + ' ' + filename + ' ' + '>' + ' ' + 'ok!')
            num_threads = int(threading_spyder.activeCount())
            print('线程数:%d') % num_threads


print('多线程,请准备好强制退出python.(任务管理器etc.)')
print('图片储存在' + ' ' + os.getcwd() + ' ' + '目录下images文件夹')
if os.path.exists('images') == True:
    pass
else:
    os.mkdir('images')
threads = []
for i in range(mp.cpu_count()):
    t1 = threading_spyder.Thread(target=producer, name='p1')
threads.append(t1)
t1.setDaemon(False)
for i in range(mp.cpu_count()):
    t2 = threading_spyder.Thread(target=customer, name='c1')
threads.append(t2)
t2.setDaemon(False)
for i in range(mp.cpu_count()):
    t3 = threading_spyder.Thread(target=customer, name='c2')
threads.append(t3)
t3.setDaemon(False)
for i in range(mp.cpu_count()):
    t4 = threading_spyder.Thread(target=customer, name='c3')
threads.append(t4)
t4.setDaemon(False)
for i in range(mp.cpu_count()):
    t5 = threading_spyder.Thread(target=customer, name='c4')
threads.append(t5)
t5.setDaemon(False)
for i in range(mp.cpu_count()):
    t6 = threading_spyder.Thread(target=customer, name='c5')
threads.append(t6)
t6.setDaemon(False)
print('检查线程...')
print('线程列表:')
print(threads)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
