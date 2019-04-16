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
