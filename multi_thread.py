#encoding: utf-8

import threading
import time

# def greet(index):
#     print 'hello world-%d' % index
#     time.sleep(0.5)
#
#
# def line_run():
#     for x in range(5):
#         greet(x)
#
# def async_run():
#     for x in range(5):
#         th = threading.Thread(target=greet,args=[x])
#         th.start()

import random

gLock = threading.Lock()
money=int(0)
def Procuder():
    while True:
        global money
        random_money = random.randint(10,100)
        gLock.acquire()
        MONEY += random_money
        gLock.release()
        print '生产者%s-生产了%d' % (threading.current_thread,random_money)
        time.sleep(0.5)
        num_threads = threading.activeCount()
        print(num_threads)
def Customer():
    while True:
        global money
        random_money = random.randint(10,100)
        if money > random_money:
            print '消费者%s-消费了：%d' % (threading.current_thread,random_money)
            gLock.acquire()
            MONEY -= random_money
            gLock.release()
        else:
            print '需要消费的钱为：%d，余额为：%d，' % (random_money,money)
        time.sleep(0.5)
        num_threads = threading.activeCount()
        print(num_threads)
def p_c_test():
    # 执行3个线程，来当作生产者
    for x in range(10):
        th = threading.Thread(target=Procuder)
        th.start()
    # 执行3个线程，来当作消费者
    for x in range(10):
        th = threading.Thread(target=Customer)
        th.start()

if __name__ == "__main__":
    # line_run()
    # async_run()
    p_c_test()
