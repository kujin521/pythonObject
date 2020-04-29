#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  : 寻觅
# @File    : 对称关系.py
# @Time    : 2019/10/30 22:45
# @Software: PyCharm


def symmetric(contrast):
    """
    :param contrast: 传入一个对偶序列R
    :return: 输出对称关系判断结果
    """
    # 将判断结果设置为result
    result = True
    # 创建一个空集合用来存储被反向后的序列
    reverse = []
    # 遍历对偶序列R给i
    for i in contrast:
        # 将每个遍历出来的i反向
        j = i[::-1]
        # 将反向后的内容存入之前建立的新序列
        reverse.append(j)
    # 将新序列自动排序（原本序列在输入时已经排序过）
    reverse.sort()
    # 对比序列看是否一样，如果不一样就不是对称关系
    if reverse != contrast:
        result = False
    return result
