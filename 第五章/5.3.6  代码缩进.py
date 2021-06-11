# -*- coding: utf-8 -*-
"""
	代码缩进
"""

'''
	以下为顺序结构的代码，并且缩进都相同
'''
# 实战圈成员列表  list
name_python = ['刘德华', '杨幂', 'Tfboys', ['Nelson', 'Bill', 'Willem']]

'''
第一种方法：赋值的方法
'''
# 修改 LIST的值
fuzhi_name_python = name_python
print(f'fuzhi_name_python: {fuzhi_name_python}')

name_python.append('扶摇')
print(f'name_python:{name_python}')
print(f'fuzhi_name_python: {fuzhi_name_python}')



# 错误例
print(f'fuzhi_name_python: {fuzhi_name_python}')
