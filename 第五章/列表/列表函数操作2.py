#功能（6）:降序排序
score_list= [90, 80, 70, 98, 50, 75, 85, 95, 100]
score_list.sort(reverse=True)
print('降序排序后:',score_list)
#功能（7）：求 85 分在本班的排名
print('85 分的排名是:',score_list.index(85)+1)
#功能（8）：求最高分和最低分
print('最高分%.2f,最低分%.2f'%(max(score_list),min(score_list)))
#功能（9）：求平均成绩
score_aver=sum(score_list)/len(score_list)
print('本班的平均成绩是：%5.1f'%score_aver)
#功能（10）：删除列表
del score_list