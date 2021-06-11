# -*- coding: utf-8 -*-
"""
	列表与元组之间的转化
"""

# 预先定义一个元组
tup1 = (1,2,3,3,6,7,5,3)

# list
print(list(tup1))
print(type(list(tup1)))

# list--> tuple
names_python_pc = ['陈升','刘德华','杨幂','TFboys']

print()
print(tuple(names_python_pc))
print(type(tuple(names_python_pc)))