# -*- coding: utf-8 -*-
"""
    列表知识点：
	
		1、定义一个列表
		2、查看变量的类型（第三天内容）
		3、三种方法输出列表元素
		4、列表与字符串区别
	
"""
# 定义一个列表
# python实战圈成员列表
names_python_pc = ['陈升','刘德华','杨幂',' TFboyes']


# 查看变量的类型（第三天内容）TYPE()  --- <class 'list'>
print(type(names_python_pc))


# 三种方法输出列表元素
print(names_python_pc)
print('python实战圈成员列表{}'.format(names_python_pc))

# python 3.6
print(f'python实战圈成员列表{names_python_pc}')

# 列表与字符串区别
name = '杨幂'
print(type(name))