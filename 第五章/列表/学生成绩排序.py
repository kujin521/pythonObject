score_list= [90, 80, 70, 98, 50, 75, 85, 95, 100]
print('成绩列表',score_list)

score_list.sort(reverse=True)
print('成绩降序排序列表',score_list)
score_list.sort(reverse=False)
print('成绩升序排序列表',score_list)

print('85分的排名是',score_list.index(85)+1)
print('最高分',max(score_list),'最低分',min(score_list))
score_aver=sum(score_list)/len(score_list)
print('平均分%.1f'%score_aver)
del score_list