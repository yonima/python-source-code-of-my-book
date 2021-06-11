# -*- coding: utf-8 -*-
"""
map(函数，可迭代对象)的用法
"""
# 需求： 使用内建函数把浮点数变成整数 int()
list_float = [6.78, 25.6, 80, 97.4]
#  Python3 与 2不同
list_int = list(map(int, list_float))
print(list_int)


# 如果参数位置错了呢？
list_int = list(map(list_float, int))
print(list_int)