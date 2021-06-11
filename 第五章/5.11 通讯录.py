# -*- coding: utf-8 -*-
"""
本次实现任务：

实现通讯录：
---欢迎使用我的通讯录---
---1 查询联系人资料---
---2 插入新的联系人---
---3 删除已有联系人---
---4 退出通讯录程序---

编写代码不是COPY，而是根据需求理解，实现功能即可。
"""
"""
    实现自己的通讯录
"""
print('---欢迎使用我的通讯录---')
print('---1 查询联系人资料---')
print('---2 插入新的联系人---')
print('---3 删除已有联系人---')
print('---4 退出通讯录程序---')

# 构建空的通讯录
addressDict = {}

# 构造死循环，推荐while 1
while True:
	# 与用户交互 ：易错点：忘记 int
    userIput = int(input('请输入指令（1 2 3 4）:'))
    
    # IF - continue  IF  IF IF
    if userIput == 1:
        # 查找联系人
        searchName = input('请输入查询人的名字：')
        
        # 使用 FOR
        if searchName in addressDict.keys():
            # 如果名字存在
            print(f"您查找的是 {searchName}， 电话是{addressDict[searchName]}")
        else:
            print('查无此人')

    elif userIput == 2:
        # 添加联系人
        addName = input("输入你要增加的人名：")
		
		# 不要遗漏
        if addName in addressDict.keys():
            # 如果添加的人已存在
            print('您输入的姓名已存在')
        else:
            addNum = input('输入他的电话号码：')
            addressDict[addName] = addNum
            print('添加联系人成功！')

    elif userIput == 3:
        # 删除联系人
        delName = input('请输入你要删除名字：')
        
        if delName in addressDict:
            del addressDict[delName]
            print('删除成功！')
        else:
            print('删除失败，查无此人！')

    elif userIput == 4:
        # 退出
        print("---感谢使用通讯录程序---")
        break

    else:
        print('请输入正确的指令:1 2 3 4')
    