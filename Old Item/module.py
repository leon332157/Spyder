# coding=utf8
import platform
import os

if not platform.system() == 'Darwin':
    print('请在OS X 运行（mac）')
    exit()
else:
    if not os.getuid() == 0:
        print('需要超级用户（root）权限！')
        exit()
    else:
        pass
os.system('easy_install pip')
os.system('pip install bs4')
os.system('pip install requests')
os.system('pip install lxml')
os.system('pip install echarts-python')
