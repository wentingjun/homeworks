# 第一周第一题
# 随机产生50个数字，存一个列表中 list，然后从小到大排序
import random
a=[int(random.random()*100) for i in range(50)]
print(a)
a.sort()
print(a)

# 然后写入文件，然后从文件中读取出来文件内容
f=open('D:\\第六周第一题.txt','w')
f.write(str(a))
f.close()

# 然后反序，在追加到文件的下一行中
a.reverse()
print(a)
f=open('D:\\第六周第一题.txt','a')
f.write(str(a))
f.close()

# 第二题
import pandas as pd

#任意的多组列表
a = [1,2,3,4,5]
b = ['mayi','jack','ton','rain','hanmeimet']    
c = [18,21,25,19,23]
d = [99,89,95,80,81]

#字典中的key值即为csv中列名
dataframe = pd.DataFrame({'No.':a,'Name':b,'Age':c,'Score':d})
dataframe = dataframe[['No.','Name','Age','Score']]

#将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv("D:\\t.csv",index=False,sep=',')

