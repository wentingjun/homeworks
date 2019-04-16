#通讯录设置
# 创建于2019.04.02

print('-----菜单------')
print('1.增加姓名和手机')
print('2.删除姓名')
print('3.修改手机')
print('4.查询所有用户')
print('5.根据姓名查找手机号')
print('6.退出')
print()

n=int(input('请输入执行命令号码（1-6）：'))

Tell_book={'A':1234,'B':1562,'C':6579}
while(n!=6):   #限定输入
    while (n>6):
        print('-----菜单------')
        print('1.增加姓名和手机')
        print('2.删除姓名')
        print('3.修改手机')
        print('4.查询所有用户')
        print('5.根据姓名查找手机号')
        print('6.退出')
        print()
        n=int(input('输入错误，请重新输入执行命令号码（1-6）：'))
    if n==1:
        name_=input('请输入需要新增联系人姓名：')
        if (name_ in Tell_book):
            i=int(input("已有该联系人，查询联系人电话请输入'11',修改联系人电话请按'12',新增其他联系人请输入'13':"))
            if i==11:
                print('该联系人电话为：',Tell_book[name_])
            if i==12:
                number=input('请输入更正后的电话号码：')
                Tell_book[name_]=number
            if i==13:
                name_=input('请输入需要新增联系人姓名：')
                number=input('请输入联系人的电话号码：')
                Tell_book[name_]=number
                print('新增联系人完毕')  
        else:
            number=input('请输入联系人的电话号码：')
            Tell_book[name_]=number
            print('新增联系人完毕') 
        n=int(input('请输入执行命令号码（1-6）：'))        
    elif n==2:
        name_=input('请输入需要删去的联系人姓名：')
        while (name_ not in Tell_book) :
            name_=input('无此联系人，请重新输入需要删去的联系人姓名：')
        del Tell_book[name_]
        n=int(input('请重新输入执行命令号码（1-6）：'))
    elif n==3:
        name_=input('请输入需要修改电话的联系人姓名：')
        while (name_ not in Tell_book) :
            name_=input('无此联系人，请重新输入需要修改电话的联系人姓名：')
        number=input('请输入更正后的电话号码：')
        Tell_book[name_]=number
        n=int(input('请重新输入执行命令号码（1-6）：'))
    elif n==4:
        print(Tell_book.keys())
        n=int(input('请重新输入执行命令号码（1-6）：'))
    elif n==5:
        name_=input('请输入需要查找的联系人姓名：')
        while (name_ not in Tell_book) :
            name_=input('无此联系人，请重新输入需要查找的联系人姓名：')
        print('该联系人电话为：',Tell_book[name_])
        n=int(input('请重新输入执行命令号码（1-6）：'))