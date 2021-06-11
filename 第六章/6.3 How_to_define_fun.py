# -*- coding: utf-8 -*-
"""
如何定义函数

需求：输出"北京欢迎你"

"""
# 从 print() 到 函数
print('北京欢迎你')


# 定义函数
def welcome_beijing():
	print('北京欢迎你！')


# 带有参数的函数
def welcome_beijing(name):
	print(f'{name}, 北京欢迎你！')
	
	
# 无参数的函数调用
welcome_beijing()

# 带有参数的函数调用
welcome_beijing('刘德华')
welcome_beijing('小码哥')
welcome_beijing('杨幂')
