# -*- coding: utf-8 -*-
"""
    项目实战：《延禧攻略》之魏璎珞请客之道

功能点：

		1.列出所有人的列表，并用3种方法打印信息
		2.小嘉嫔拒绝邀请，并且打印不能参加的人
		3.尔晴参加，请重新修改列表，打印出邀请的名单。
		4.地点从延禧宫变成 御花园
		5. insert方法把‘哥哥’放在邀请名单的开头；append方法把‘傅恒’放着名单最后。
		5.1.请重新打印所有人的名单，并且使用len方法打印出，一共邀请了多少人 ，并且复制一个新的列表备份。
		6.打印前与后三个人的名字，并颠倒了一下顺序。
		7.地点从御花园变成延禧宫，只请皇后和尔晴，告知依然在受邀之列。
		8.删除多余人员，并告知"特别遗憾不能邀请大家吃饭"。
		9.del删除名单。
"""
'''
	1.列出所有人的列表，并用3种方法打印信息
'''
print('=====================================')
print('*')
print('* 1.列出参加宴会的列表，并用 3种方法打印信息')
print('*')
print('=====================================')

# 根据项目描述创建列表
fete_list = ['太后','皇后','纯妃','小嘉嫔','舒妃','皇上']

# 第一种方法：把所有人的信息都打印在一起
print('第一种方法打印列表')
print(f'春节将至，请 {fete_list} 过来延禧宫小聚.')

# 第二种方法:for循环给每一个人打印一条消息 -- 第五天内容
print(' ')
print('第二种方法:for循环给每一个人打印一条消息')

for name in fete_list:
    print(f'春节将至，请 {name} 过来延禧宫小聚.')
    
# 第三种方法，使用索引访问每一个元素
print(' ')
print('第三种方法，使用索引访问每一个元素')
print(f'春节将至，请 {fete_list[0]} 过来延禧宫小聚.')
print(f'春节将至，请 {fete_list[1]} 过来延禧宫小聚.')
print(f'春节将至，请 {fete_list[2]} 过来延禧宫小聚.')
print(f'春节将至，请 {fete_list[3]} 过来延禧宫小聚.')
print(f'春节将至，请 {fete_list[4]} 过来延禧宫小聚.')
print(f'春节将至，请 {fete_list[5]} 过来延禧宫小聚.')

# 注意索引小标： print(f'春节将至，请 {fete_list[6]} 过来延禧宫小聚.')

'''
    2.小嘉嫔拒绝邀请，并且打印不能参加的人
'''
print('=====================================')
print('*')
print('* 2.小嘉嫔拒绝邀请，并且打印不能参加的人')
print('*')
print('=====================================')
# 注意不要直接
# print('不能参加宴会的人是: 小嘉嫔')

# 删除小嘉嫔的信息
# 区别 remove() del() pop()
index_name = fete_list.index('小嘉嫔')
# 根据索引删除，POP()删除最后一个元素
del_name = fete_list.pop(index_name)
print(f'\n\t不能参加宴会的人是: {del_name}')

# 其他方法：比如把 3与2步合并 ，直接使用index fete_list[3] = '尔晴'

print('=====================================')
print('*')
print('* 3.尔晴参加，请重新修改列表，打印出邀请的名单。')
print('*')
print('=====================================')
fete_list.append('尔晴')

print(f'\n\t添加尔晴以后的人员名单为{fete_list}')

print('=====================================')
print('*')
print('* 4.地点从延禧宫变成 御花园 -- 两种方法实现')
print('*')
print('=====================================')

# 第一种方法复制列表，copy.也是浅拷贝，也可以使用深拷贝
garden_name = fete_list.copy()
print(f'(第一种COPY：地点从延禧宫变成御花园后的人员名单{garden_name})')


# 第二种方法复制列表，使用切片
garden_name_2 = fete_list[:]
print(f'(第二种COPY：地点从延禧宫变成御花园后的人员名单{garden_name})')

print('===============')
print('*')
print('* 5. insert方法把‘哥哥’放在邀请名单的开头；append方法把‘傅恒’放着名单最后。')
print('* 5.1  请重新打印所有人的名单，并且使用len 打印出，一共邀请了多少人 ，并且复制一个新的列表备份。')
print('*')
print('=====================================')
garden_name.insert(0,'哥哥')
garden_name.append('傅恒')
print(f'\t在御花园的人员名单变成：{garden_name}')
# 使用len方法查看一共邀请多少人
total = len(garden_name)
print(f'\t魏璎珞在御花园一共邀请了{total} 人 参加宴会。')
# 备份列表
copy_garden_name = garden_name.copy()

print('=====================================')
print('*')
print('* 6.打印前与后三个人的名字，并颠倒了一下顺序。')
print('*')
print('=====================================')

# 使用切片打印
print(f'参加宴会的前三个人员是:{garden_name[:3]}')
print(f'参加宴会的后三个人员是:{garden_name[-3:]}')
# 列表反转
print(f'原来的人员顺序是{garden_name}')
garden_name.reverse()
print(f'反转以后的人员顺序是{garden_name}')

# 第二种实现方法：切片

print('=====================================')
print(' ')
print('8 .删除多余人员，并告知"特别遗憾不能邀请大家吃饭"。')
print('目前的所有宴请名单有：',garden_name)

#第一种：用remove方法删除
print('第一种：用remove方法删除')
remove_1= '太后'
garden_name.remove(remove_1)
print(f'特别遗憾不能邀请{remove_1}吃饭')
remove_2= '皇上'
garden_name.remove(remove_2)
print(f'特别遗憾不能邀请{remove_2}吃饭')
remove_3= '纯妃'
garden_name.remove(remove_3)
print(f'特别遗憾不能邀请{remove_3}吃饭')
remove_4= '舒妃'
garden_name.remove(remove_4)
print(f'特别遗憾不能邀请{remove_4}吃饭')
remove_5= '哥哥'
garden_name.remove(remove_5)
print(f'特别遗憾不能邀请{remove_5}吃饭')
remove_6= '傅恒'
garden_name.remove(remove_6)
print(f'特别遗憾不能邀请{remove_6}吃饭')

print(f'删除后的名单为：{garden_name}')

'''
#第二种方法，使用for循环
print(' ')
print('第二种方法，使用for循环')
r_list=['皇后','尔晴']
for name in garden_name:
    #print(garden_name)
    if name not in r_list:
        #index = garden_name.index(name)
        #del_name = garden_name.pop(index)
        print(f'特别遗憾不能邀请 {name} 来吃饭')

name_1 = garden_name.pop(0)
name_2 = garden_name.pop(1)
name_3 = garden_name.pop(1)
name_4 = garden_name.pop(1)
name_5 = garden_name.pop(2)
name_6 = garden_name.pop(2)

print('删除多于人员后的名单为：',garden_name)
print(f'特别遗憾不能邀请您 {name_1} 来参加宴会。')
print(f'特别遗憾不能邀请您 {name_2} 来参加宴会。')
print(f'特别遗憾不能邀请您 {name_3} 来参加宴会。')
print(f'特别遗憾不能邀请您 {name_4} 来参加宴会。')
print(f'特别遗憾不能邀请您 {name_5} 来参加宴会。')
print(f'特别遗憾不能邀请您 {name_6} 来参加宴会。')
'''

print('=====================================')
print('*')
print('* 7.地点从御花园变成延禧宫，只请皇后和尔晴，告知依然在受邀之列。')
print('*')
print('=====================================')

print(f'宴会从御花园变成延禧宫，您，{garden_name[0]},依然在邀请之列。')
print(f'宴会从御花园变成延禧宫，您，{garden_name[1]},依然在邀请之列。')

print('=====================================')
print('*')
print('* 9.删除名单。')
print('*')
print('=====================================')
del garden_name
del fete_list
del copy_garden_name