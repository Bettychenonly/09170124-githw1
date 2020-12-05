James=['Lebron James',23,19,22,31,18]
games=len(James)
score_max=max(James[1:games])
i=James.index(score_max)
print(James[0],"在第%d場得最高分%d分" %(i,score_max))

James=[['Lebron James','SF','12/30/84'],23,19,22,31,18]
games=len(James)
score_max=max(James[1:games])
i=James.index(score_max)
name,position,born=James[0][0],James[0][1],James[0][2]
print('姓名   ：',name)
print('位置   ：',position)
print('出生日期：',born)
print("在第%d場得最高分%d分" %(i,score_max))

