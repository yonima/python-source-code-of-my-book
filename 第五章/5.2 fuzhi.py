# -*- coding: utf-8 -*-
"""
	python三大拷贝方法：
	1、 =
	2、copy
	3、deepcopy
	
	# 需求：备份成员名单
"""
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

'''
第二种方法：浅拷贝 COPY
'''
# 1. COPY
copy_name_python_1 = name_python.copy()
print(f'copy_name_python_1:{copy_name_python_1}')

# 修改LIST 的值
name_python.remove('扶摇')
print(f'name_python:{name_python}')
print(f'copy_name_python_1:{copy_name_python_1}')

# 修改 子对象的值
name_python[3].append('Jack')
print('\n修改 子对象的值')
print(f'name_python:{name_python}')
print(f'copy_name_python_1:{copy_name_python_1}')

print('\n查看id是不是一样')
print(copy_name_python_1 is name_python)
print(id(copy_name_python_1), id(name_python))

print()
print(copy_name_python_1[3] is name_python[3])
print(id(copy_name_python_1[3]),id(name_python[3]))


# 第二种方法  import copy
import copy
copy_name_python_2 = copy.copy(name_python)

print('\n第二种方法  import copy ')
print(name_python)
print(f'copy_name_python_2:{copy_name_python_2}')


'''
	作业：
'''
# 修改list

# 修改 子对象

'''
第三种方法：深拷贝 deepcopy
'''
import copy
deepcopy_name_python = copy.deepcopy(name_python)
print('\n第三种方法：深拷贝 deepcopy')
print(f'name_python:{name_python}')
print(f'deepcopy_name_python:{deepcopy_name_python}')

# 修改LIST 的值
name_python.append('扶摇')
print('\n修改LIST 的值')
print(f'name_python:{name_python}')
print(f'deepcopy_name_python:{deepcopy_name_python}')

# 原理
print('\n原理')
print(id(name_python), id(deepcopy_name_python))
print(name_python is deepcopy_name_python)


# 修改 子对象的值
name_python[3].append('Tom')
print('\n修改 子对象的值')
print(f'name_python:{name_python}')
print(f'deepcopy_name_python:{deepcopy_name_python}')

# 原理
print('\n原理')
print(id(name_python), id(deepcopy_name_python))
print(name_python is deepcopy_name_python)

# 查看子对象的值
print('\n 查看子对象的值')
print(id(name_python[3]), id(deepcopy_name_python[3]))
print(name_python[3] is deepcopy_name_python[3])