#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  : 寻觅
# @File    : 传递关系.py
# @Time    : 2019/10/30 23:26
# @Software: PyCharm

from 符合关系 import add


def transmit(contrast):
    result = True
    """

    :param contrast: 传入一个对偶序列R
    :return: 输出符合关系判断结果
    """
    # 将自己进行一次符合运算
    data = add(contrast, contrast)
    for i in data:
        # count用于判断指定元素在集合中出现的次数，查看符合运算出的内容是否都为本身
        if contrast.count(i) == 0:
            result = False
    return result
