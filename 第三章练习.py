# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:06:23 2020

@author: Administrator
"""
# 查看关键字
import keyword
keyword.kwlist

#pythiobn基本输出
print("欢迎使用print函数")
name=input("请输入您的姓名：")
print('你好！',name)
print('1+2',1+2)

print(1,2,3,sep="!",end='$$$$')
print(4)
print(5,6,7)

#字符串格式化输出
'''

'''
print("我叫%s今年%d岁!" %('小明',10))

print('%2d-%02d' %(3,1))
print('%.2f' %3.1415926)

print('hello %s' %'world')
#相当于
print('hello {}'.format('world'))

print("{} {}".format("山东交通学院","学院"))
print("{0} {1}".format("山东交通学院","学院"))
print("{1} {0} {1}".format("山东交通学院","学院"))

print("姓名：{name}, 邮箱：{email}".format(name="李氏",email="www.dud@163.com"))
#数字格式化
print("{:.2f}".format(3.1415926))

#本关任务：编写一个程序完成以下任务：
#（1）以四舍五入方式输出保留n位有效小数的值。
#（2）以直接舍去的方式输出保留2位有效小数的值

#############完成第10、11、12、13行代码实现程序功能####

my_num=input()				#从测试集获取浮点型数字
my_n=input()				#从测试集获要保留的位n

my_num_float=float(my_num)				#使用float函数将my_num转换为小数
my_n_int=int(my_n)					#使用int函数将my_n转换为整数
my_num_float1=round(my_num_float,my_n_int)#采用round函数四舍五入取整
my_num_float2=float('%.2f'%my_num_float)	#巧妙采用将小数放大后取整再缩小的方式可以获取直接截取
print(my_num_float1)		#输出结果1
print(my_num_float2)		#输出结果2		
###################end################################


 #(1)a,b为两个整数
a=int(input())
b=int(input())
print('%d+%d=%d'%(a,b,a+b))             #去掉【】补充代码已实现输出a加b的值


#(1)a,b为两个小数
a=float(1.1)
b=float(1.1)
print('{:.2f}-{:.2f}={:.2f}'.format(a,b,a-b))       #去掉【】补充代码已实现输出a减b的值均保留为2位小数
print('{:.2f}-{:.2f}={:.2f}'.format(a,b,a-b))       #去掉【】补充代码已实现输出a减b的值均保留为2位小数
print('{:.2f}*{:.2f}={:.2f}'.format(a,b,a*b))       #去掉【】补充代码已实现输出a减b的值均保留为2位小数
print('{:.2f}/{:.2f}={:.2f}'.format(a,b,a/b))       #去掉【】补充代码已实现输出a减b的值均保留为2位小数

#【例 3.13】字符串运算符示例。
print('123'+'abc') #字符串连接
print('Hello\nworld') #\n 转义字符表示换行
print('-'*18) #输出 18 个-
print(r'Hello\nworld') #取消转义
print('el' in 'Hello') #字符串包含测试

print('%d/%d=%.17f'% (35,45,35/45))            #去掉【】补充代码已实现输出a除以b的值

print("BMI是{}".format(float(1.6/50)))   #去掉【】补充代码

h,w = eval(input()) # 请输入身高(m)和体重(kg)，英文逗号隔开，
print("BMI是{:.1f}".format(float(w/h**2)))   #去掉【】补充代码

#（1）从键盘输入一个整数和一个字符，以逗号隔开，在屏幕上显示输出一条信息。
a,x =input("请输入1个整数和1个符号，逗号隔开").split(',')     # 去掉【】补充代码，请输入1个整数和1个符号，逗号隔开
print(x*eval(a),a,x*eval(a))   # 去掉【】补充代码

#（2）如何对3.1415926进行输出，输出为3.14%
print("{:.2f}%".format(3.1415926))   #去掉【】补充代码已实现输出3.14%

F=eval(input())
C=5/9*(F-32)                    		 #去掉【】补充代码以实现温度转换
print('华氏温度{}转换为摄氏温度为{:.2f}'.format(F,C))  
#去掉【】补充代码以实现结果，例如：华氏温度110转换为摄氏温度为43.33

#输入圆半径，求圆周长和圆面积
r=eval(input())    #去掉【】补充代码以实现获取输入半径的值
PI=3.1415926
L=2*PI*r             #去掉【】补充代码以实现计算圆周长
S=PI*r**2			#去掉【】补充代码以实现计算面积
print("圆周长为"+"{:.2f}".foramt(L)+",面积为"+"{:.2f}".foramt(S))        #去掉【】补充代码以实现输出：保留两位小数的圆周长和圆面积
#例如：输出结果示例1：圆周长为113.10,面积为1017.88













