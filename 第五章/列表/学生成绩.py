score_list=[]
print('请逐个输入学生成绩，用空格分隔，以回车结束')
score_str=input()
temp=score_str.split(' ')
for str in temp:
    score_list.append(int(str))

print('成绩列表：',score_list)
print('第一个成绩',score_list[0],'最后一个成绩',score_list[-1])
score_list[3]=98
print('第四个成绩更新后',score_list)
del score_list[5]
print('删除第六个成绩',score_list)

score_top5=score_list[:5]
print('前五个成绩',score_top5)
score_last5=score_list[-1:6:-1]
print('后五个成绩',score_last5)