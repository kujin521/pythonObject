'''任务：输入一个整数num，用range()函数产生一个从num开始的10个整数组成的列表listx;
将列表listx中的每个元素的值乘以2，形成一个新的列表listy，输出两个列表。
'''
#####请在下面标有序号的注释后面填写程序#####
# (1)输入整数num
num=int(input())

# (2)用range()函数产生列表 listx
listx=list(range(1, 11))

# 输出列表
print(listx)

# (3)将列表listx中的每个元素的值乘以2，形成一个新的列表listy
listy=[x*2 for x in listx]
# 输出列表
print(listy)

#####　程序结束　　#####