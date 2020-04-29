# 创建列表
list1=list()
list2=[]
# 添加元素
list1.append('第一个元素')# 添加到末尾
list2.insert(1,'inset')# 添加到指定位置
list1.extend(list2)# 添加列表

list1.append("再添加一个")
list1.append("再添加二个")
list1.append("再添加个")
# 修改列表
list1[0]='修改元素'
# 删除元素
del list1[1]
list1.pop(1)
list1.remove("再添加二个")

print(list1,list2)