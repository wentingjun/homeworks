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