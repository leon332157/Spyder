# coding=gbk
# ���������������ݵ�
# requests
# pip install requests
# ��������html�ĵ���Ȼ�����������Ҫ������
# beautifulsoup4
# pip install bs4
# lxml�⣬��������
# pip install lxml
# ������ʹ��linux���뽫�鿴����˵��������
# coding=utf8
print('���ģ��Ϳ�...')
import os
import time
import sys
import platform

try:
    import requests
    import urllib
    from bs4 import BeautifulSoup
    import threading_spyder
    import thread
    import multiprocessing as mp
    import lxml

    time.sleep(1)
    print('���!')
except ImportError:
    print('ģ����δ��װ! ���ڻ�ȡ...')
    if platform.system() is 'Windows':
        os.system('C:\Python27\Scripts\pip.exe install bs4')
        os.system('C:\Python27\Scripts\pip.exe install requests')
        os.system('C:\Python27\Scripts\pip.exe install urllib3')
        os.system('C:\Python27\Scripts\pip.exe install requests')
        os.system('C:\Python27\Scripts\pip.exe install lxml')
    elif platform.system() is 'windows':
        os.system('C:\Python27\Scripts\pip.exe install bs4')
        os.system('C:\Python27\Scripts\pip.exe install requests')
        os.system('C:\Python27\Scripts\pip.exe install urllib3')
        os.system('C:\Python27\Scripts\pip.exe install requests')
        os.system('C:\Python27\Scripts\pip.exe install lxml')
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
    print('���!')
BASE_PAGE_URL = 'http://www.doutula.com/photo/list/?page='
# ҳ���url�б�
PAGE_URL_LIST = []
# ���еı����url���б�
FACE_URL_LIST = []
# ȫ����
gLock = threading_spyder.Lock()
for x in range(1, 50):
    url = BASE_PAGE_URL + str(x)
    PAGE_URL_LIST.append(url)
print('��ַ= %s' % PAGE_URL_LIST)


def download_image(url):
    # ��ͼƬ��������
    # ָ��ͼƬ����·��
    # ���������һ������
    split_list = url.split('/')
    filename = split_list.pop()
    path = os.path.join('images', filename)
    urllib.urlretrieve(url, filename=path)


def producer():
    while True:
        gLock.acquire()
        if len(PAGE_URL_LIST) == 0:
            gLock.release()
            print('url����')
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
        exit()


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
            print('�߳���:%d') % num_threads
    exit()


time.sleep(1)
print('���߳�,��׼����ǿ���˳�python.(���������etc.)')
print('ͼƬ������' + ' ' + os.getcwd() + ' ' + 'Ŀ¼��images�ļ���')
threads = []
time.sleep(1)
print('����,����߳�...')
for i in range(mp.cpu_count()):
    main = threading_spyder.Thread(name='MainThread')
threads.append(main)
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
print('�߳��б�(p=��ȡ,c=����):')
print(threads)
time.sleep(1)


def thread_start():
    if os.path.exists('images') == True:
        pass
    else:
        os.mkdir('images')
    fff = raw_input('��ʼ? ��Ҫǿ���˳�! r�˳�!(y/n/r):')
    if fff is 'y':
        t1.start()
        t12.start()
        t13.start()
        time.sleep(1)
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
        print('�˳�!')
        exit()
    else:
        print('�������!')
        thread_start()
        pass


thread_start()
