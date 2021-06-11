# -*- coding: utf-8 -*-
"""
元组知识点：

	什么是元组？

	如何修改元组的值？两个方法

	元组内置方法

"""

'''
什么是元组？创建元组的几种方法
'''
# 1、直接使用,
tup1 = 1, 2, 3
print('直接使用, : ',tup1)
print(type(tup1))
# list -- 列表 str ---字符串  tuple -- 元组

# 2、使用()
tup2 = (1, 2, 3)
print('\n使用() : ',tup2)
print(type(tup2))

# 3、创建一个元素的元组
print()
tup3 = ( 1 )
print(type(tup3))

tup4 = (1, )
print('\n tup4 :',type(tup4))

# 4、创建空元组
tup5 = ( )
print('\n tup5', type(tup5))

# 5、使用tuple()函数创建元组

# 将字符串创建为元组
print(tuple('Python'))

# 将列表创建为元组
print(tuple(['Python','Java', 'C++']))

# 6、创建元组的元组
tup7 = ('P', 'y', 't', 'h', 'o', 'n'), ('Python', 'Java', 'C++')
print(tup7)

# 7、元组拼接 + 列表拼接 + extend() * 3
tup8 = ('P', 'y', 't', 'h', 'o', 'n') + ('Python', 'Java', 'C++')
print('\n tup8', tup8)

'''
如何修改元组的值？两个方法
'''
# 不能修改的例子
tup_ex = ('Python',[1,2,3],'Java')

# 索引的方法
# tup_ex[2] = 'C++'
# print(tup_ex)

# 创建还有列表的元组
tup_ex[1].append(4)
print('\n修改元组中列表的值',tup_ex)

# 修改元组变量的值
tup_ex = (1, 2 ,3)
print('\n修改后的tup_ex：',tup_ex)

# 删除整个元组
# del tup_ex
# print(tup_ex)

'''
元组内置方法
'''
tup1 = (1,3,3,3,5,6,7,8,9)

# count(3) 计算出现的次数
print('count(3) 计算出现的次数', tup1.count(3))

# max()
print(max(tup1))

# min()
print(min(tup1))

# len()
print(len(tup1))

# index()
print(tup1.index(5))