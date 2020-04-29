#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/10/30 9:03
# @Author  : 寻觅
# @File    : 主模块. py
# @Software: PyCharm

from 用户输入 import write_a as 输入A, write_r as 输入R
from 自反关系 import introspect as 自反关系判断
from 对称关系 import symmetric as 对称关系判断
from 传递关系 import transmit as 传递关系判断
from 符合关系 import add as 符合运算
from 自反闭包 import reverse as 自反闭包计算
from 函数及其类型 import fn as 函数判断


# 用来接收write_r模块的
def 输入R精简版():
    重复 = True
    while 重复:
        输入 = 输入R()
        重复 = 输入[0]
        内容 = 输入[1]
        if 重复:
            print(内容)
    return 内容


# 做用户输入判断
程序重复 = True
while 程序重复:

    print("""
    请输入你需要执行的功能的序号！
    1.判读自反关系
    2.判读对称关系
    3.判读传递关系
    4.对两个关系进行复合
    5.输出自反闭包
    6.判读是否为函数以及函数类型
    """)

    输入判断 = True
    while 输入判断:
        序号 = input('请输入相应的数字：  ')
        # isdigit用于判断是否为数字
        if 序号.isdigit():
            序号 = int(序号)
            if 1 <= 序号 <= 6:
                输入判断 = False
            else:
                print('请输入数字1或2或3或4或5或6')
        else:
            print('请数字一个整数')
    # 将类（Relation）进行实例化处理

    if 序号 == 1:
        A = 输入A()[1]
        R = 输入R精简版()
        自反关系 = 自反关系判断(A, R)
        if 自反关系:
            print('你输入%s和%s\n是自反关系\n' % (A, R))
        else:
            print('你输入%s和%s\n不是自反关系\n' % (A, R))

    elif 序号 == 2:
        R = 输入R精简版()
        对称关系 = 对称关系判断(R)
        if 对称关系:
            print('你输入的%s\n是对称关系\n' % R)
        else:
            print('你输入的%s\n不是对称关系\n' % R)

    elif 序号 == 3:
        R = 输入R精简版()
        传递关系 = 传递关系判断(R)
        if 传递关系:
            print('你输入的%s\n是传递关系\n' % R)
        else:
            print('你输入的%s\n不是传递关系\n' % R)

    elif 序号 == 4:
        print('请输入第一组')
        R1 = 输入R精简版()
        print('请输入第一组')
        R2 = 输入R精简版()
        符合运算结果 = 符合运算(R1, R2)
        print('两对关系相加后的结果为：', 符合运算结果, '\n')

    elif 序号 == 5:
        A = 输入A()[1]
        R = 输入R精简版()
        自反闭包 = 自反闭包计算(A, R)
        print('自反闭包为：', 自反闭包)

    elif 序号 == 6:
        A = 输入A()[0]
        B = 输入A()[0]
        R = 输入R精简版()
        函数 = 函数判断(A, B, R)
        if 函数[0]:
            print('\n这是函数,', end='')
        else:
            print('\n这不是函数,', end='')
        if 函数[1]:
            print('是单射,', end='')
        else:
            print('不是单射,', end='')
        if 函数[2]:
            print('是满射\n',)
        else:
            print('不是满射\n',)

    异常 = True
    while 异常:
        程序重复 = input('请输入是否继续执行？（‘是’、‘yes’、‘1’为继续程序，‘否’、‘no’、‘0’为结束程序）')
        if 程序重复 == '是' or 程序重复 == 'yes' or 程序重复 == '1':
            异常 = False
        elif 程序重复 == '否' or 程序重复 == 'no' or 程序重复 == '0':
            程序重复 = False
            异常 = False
        else:
            print('输入有误，请重新输入')

