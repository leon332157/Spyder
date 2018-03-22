# encoding: utf-8
# 用来请求网络数据的
# requests
# pip install requests
# 用来解析html文档，然后过滤我们需要的数据
# beautifulsoup4
# pip install bs4
import platform
import os
import time

print('检查模块...')
try:
    import requests
    import urllib
    from bs4 import BeautifulSoup
    import threading_spyder
    import thread
    import multiprocessing as mp

    time.sleep(1)
    print('完成!')
except ImportError:
    print('模块未安装! 正在获取...')
    if platform.system() is 'windows':
        os.system('C:\Python27\Scripts\pip.exe install bs4')
        os.system('C:\Python27\Scripts\pip.exe install requests')
        os.system('C:\Python27\Scripts\pip.exe install urllib')
        os.system('C:\Python27\Scripts\pip.exe install requests')
    else:
        os.system('pip install bs4')
        os.system('pip install requests')
        os.system('pip install urllib')
        os.system('pip install requests')
    import requests
    import urllib
    from bs4 import BeautifulSoup
    import threading_spyder
    import thread
    import multiprocessing as mp

    time.sleep(1)
    print('完成!')
BASE_PAGE_URL = 'http://www.doutula.com/photo/list/?page='
# 页面的url列表
PAGE_URL_LIST = []
# 所有的表情的url的列表
FACE_URL_LIST = []
# 全局锁
gLock = threading_spyder.Lock()
for x in range(1, 2):
    url = BASE_PAGE_URL + str(x)
    PAGE_URL_LIST.append(url)
print('url= %s' % PAGE_URL_LIST)


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
            print('url错误')
            break
        else:
            page_url = PAGE_URL_LIST.pop()
            print(page_url)
            gLock.release()
            response = requests.get(page_url)
            print(response)
            content = response.content
            print(content)
            soup = BeautifulSoup(content, 'lxml')
            print(soup)
            img_list = soup.find_all('img', attrs={'class': 'img-responsive lazy image_dta'})
            print(img_list)
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
            print('Download' + ' ' + filename + ' ' + '>' + ' ' + path + ' ' + 'ok!')
            num_threads = int(threading_spyder.activeCount())
            print('线程数:%d') % num_threads
    exit()


time.sleep(1)
print('多线程,请准备好强制退出python.(任务管理器etc.)')
print('图片储存在' + ' ' + os.getcwd() + ' ' + '目录下images文件夹')
threads = []
time.sleep(1)
print('创建,检查线程...')
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
for i in range(mp.cpu_count()):
    t7 = threading_spyder.Thread(target=customer, name='c6')
threads.append(t7)
t7.setDaemon(False)
for i in range(mp.cpu_count()):
    t8 = threading_spyder.Thread(target=customer, name='c7')
threads.append(t8)
t8.setDaemon(False)
for i in range(mp.cpu_count()):
    t9 = threading_spyder.Thread(target=customer, name='c8')
threads.append(t9)
t9.setDaemon(False)
for i in range(mp.cpu_count()):
    t10 = threading_spyder.Thread(target=customer, name='c9')
threads.append(t10)
t10.setDaemon(False)
for i in range(mp.cpu_count()):
    t11 = threading_spyder.Thread(target=customer, name='c10')
threads.append(t11)
t11.setDaemon(False)
for i in range(mp.cpu_count()):
    t12 = threading_spyder.Thread(target=producer, name='p2')
threads.append(t12)
t12.setDaemon(False)
for i in range(mp.cpu_count()):
    t13 = threading_spyder.Thread(target=producer, name='p3')
threads.append(t13)
t13.setDaemon(False)
time.sleep(1)
print('线程列表(p=爬取,c=下载):')
print(threads)
time.sleep(1)


def thread_start():
    if os.path.exists('images') == True:
        pass
    else:
        os.mkdir('images')
    fff = raw_input('开始? 需要强制退出! r退出!(y/n/r):')
    if fff is 'y':
        t1.start()
        t12.start()
        t13.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()
        t11.start()
    elif fff is 'n':
        thread_start()
    elif fff is 'r':
        exit()
    else:
        print('输入错误!')
        thread_start()
        pass


thread_start()
