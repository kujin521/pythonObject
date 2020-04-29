#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  : 寻觅
# @File    : 函数及其类型.py
# @Time    : 2019/10/31 0:13
# @Software: PyCharm


def fn(fn1, fn2, contrast):
    """

    :param fn1: 传入第一个集合
    :param fn2: 传入第二个集合
    :param contrast: 传入序列R
    :return: 输出按顺序分别是‘是否是函数’，‘是否单射’，‘是否满射’
    """
    # 建立一个data列表，之后用来判断是否是满射会用
    data = []
    # 默认是函数
    result = True
    # 默认不是单射和满射
    single = False
    full = False
    # 判断如果集合与序列长度不一样，哪肯定不是函数
    if len(fn1) != len(contrast):
        result = False
    else:
        # 用来判断fn1是否有问题
        n = 0
        while len(fn1) > n:
            # count函数用来判断列表中有几个指定的元素，如果发现序列R中并非有且只有一个集合fn1中的元素这就不是一个函数。
            if fn1.count(contrast[n][0]) != 1:
                result = False
                break
            n += 1
        # 用来判断fn2是否有问题
        n = 0
        while len(fn2) > n:
            # 先将序列R中对应fn2位置的函数都取出存放到一个新的列表中
            data.append(contrast[n][1])
            # 查看是否有序列R中的元素在fn2中并没有出现的情况出现，如果有就表示这不是函数
            if fn2.count(contrast[n][1]) == 0:
                result = False
                break
            # 判断是否是单射
            elif fn2.count(contrast[n][1]) == 1:
                single = True
            n += 1

        # 将序列R中拿出的一组新列表和fn2都进行一次排序
        data.sort()
        fn2.sort()

        # 判断fn2和data是否完全相等，来判断是否是满射
        if fn2 == data:
            full = True

    return result, single, full
