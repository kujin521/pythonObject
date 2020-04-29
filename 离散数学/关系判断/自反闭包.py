#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  : 寻觅
# @File    : 自反闭包.py
# @Time    : 2019/10/30 23:54
# @Software: PyCharm

from 自反关系 import introspect


def reverse(original, contrast):
    """

    :param original: 传入一个自反函数A
    :param contrast: 传入一个对偶序列R
    :return: 输出自反闭包
    """
    # 判断输入是否就自反函数，如果是，就直接输出R
    if introspect(original, contrast):
        return contrast
    # 如果不是就将A和R相加
    else:
        data = original + contrast
        # 将加完后的内容取出检查是否有重复的
        for i in data:
            # count函数用来判断列表中有几个指定的元素，将重复的内容删除
            if data.count(i) > 1:
                data.remove(i)
        return data
