# 介绍
```angular2
我们现在有一个需求，具体需求内容如下
（1） 判断关系R是否为自反关系。键盘输入R的关系序偶，程序输出判断结果
（2） 判断关系R是否为对称关系。键盘输入R的关系序偶，程序输出判断结果
（3） 判断关系R是否为传递关系。键盘输入R的关系序偶，程序输出判断结果
（4） 键盘输入两个已知关系通过合成构造新的关系，程序输出复合后的新关系
（5） 键盘输入关系R序偶，程序计算该关系的自反闭包，并输出结果。
（6） 键盘输入关系R序偶，程序判断该关系是否为函数与函数类型，并输出判断结果。

我使用Python模块化开发思路将每一项需求都进行开发。并有详细注释，所以我就直接上代码了。

代码
根据题意我们的知，我们需要输入两种类型的内容，所以我就做了一个用户输入的模块,然后是个个需求处理模块。

```

## 用户输入
```python
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

```
## 自反关系
```python
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
```

## 对称关系
```python
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
```

## 传递关系
传递关系需要用到符合关系的一些判断，所以在这里我就直接引入符合关系对函数进行一些处理
```python
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
```

## 自反闭包
```python
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
```

## 函数及其类型
```python
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
```

## 主函数
主函数内我所有变量都用的是中文，我试了我的两台Windows10系统，pycharm编译器，Python3.8版本情况下没有报错，只有一些让我使用ASCII编码的提示，但是并不影响程序运行！
```python
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
```
