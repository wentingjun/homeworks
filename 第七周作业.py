import numpy as np  
import matplotlib.pyplot as plt 
import csv 
 
# 读取并存放文件里的数据 
data=[]  
with open('d:/三5.csv','r+') as f : 
     for row in csv.reader(f):         
          for i in range(0,21): 
             data.append(row[i]) 
data=np.array(data).reshape(44,21)
score=np.array(data[1:43,5:21],dtype=float) 
print(score)

x=np.arange(1,17)
for i in range(42): 
    plt.title(data[i+1,0]) 
    plt.xlabel('score') 
    plt.ylabel('exams dates') 
    plt.plot(x,label='Score line')
    plt.plot(x,score[i],'ro-')  
    plt.legend('Score line')
     #  纵坐标的显示范围是0到100
    plt.ylim(0,100) 
    plt.xticks(x,data[0,5:21]) 
     #  命名
    param=dict( 
    fname=data[i+1,3], 
    figtype='jpg' 
    ) 
    plt.savefig(**param) 
    # plt.show()
    plt.clf()

