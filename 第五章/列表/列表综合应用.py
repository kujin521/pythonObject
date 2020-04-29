'''任务：输入一个班的学生的身高，找出能作为升旗手的学生身高有哪些？ 共多少人？
'''
##### 请在下面标注序号的位置填写程序#####
# 输入多个身高（单位：cm），用逗号分隔
highList = list(eval(input()))

# (1) 找出身高在170~175之间的
hights=[x for x in highList if x>=170 and x<=175]

# (2)输出可选身高列表
print(hights)

# (3) 输出可选身高人数
print(len(hights))

#####  程序结束  #####