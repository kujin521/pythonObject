#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/10/30 9:03
# @Author  : 寻觅
# @File    : 用户输入. py
# @Software: PyCharm


# 用于接收集合a的函数
def write_a():
    """
    :return: 输出按位置分别是‘集合’，'自反集合'
    """
    # 创建一个列表用于存储自反集合
    original = []
    # 将接收的集合保存到data中
    data = input('请输入集合（数字间请用逗号隔开）').split(',')

    # 将收到的集合自动转换为自反集合并存储到original中
    n = 0
    for i in data:
        original.append([i, i])
        n += 1
    print('你输入的集合为', data, '你输入的自反集合为', original)
    return data, original


# 用于接收对偶序列R的的函数
def write_r():
    """

    :return: 当程序出现异常，将会输出异常和异常信息，当程序正常运行将会输出正常信息和自动排序后的对偶序列
    """
    # 创建接收对偶序列的序列
    contrast = []
    # 接收用户需要输入几对对偶序列的信息，并做容错处理，如果用户输入内容不是整数则抛出异常
    try:
        custom = int(input('你要输入几对对偶序列？'))
    except Exception as abnormal:
        data = '异常被抛出，异常内容为：%s！\n(输入内容必须是一个整数，请重新输入一个整数）' % abnormal
        repeat = True
        return repeat, data
    else:
        repeat = False
        # 如果没有抛出异常，开始对用户输入进行处理
        i = 0
        while custom > i:
            i += 1
            print('正在输入', i, '对关系序列,按回车键后输入下一对')
            n = True
            # 用户进行输入并判断是否合法
            while n:
                r = input('对关系中每个元素用逗号隔开：  ').split(',')
                if len(r) != 2:
                    print('你输入的值有误，请输入有且仅有一对关系！')
                elif len(r) == 2:
                    contrast.append(r)
                    n = False
        # 对用户输入的序列自动排序，方便后续处理
        contrast.sort()
        print('需要对比的序列经过自动排序后为', contrast)
        return repeat, contrast
