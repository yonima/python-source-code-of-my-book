# -*- coding: utf-8 -*-
"""
函数参数： 形参 VS 实参

需求：请输出以下内容：
刘德华, 北京欢迎你！
小码哥, 北京欢迎你！
杨幂, 北京欢迎你！
"""


# 定义函数
def welcome_beijing():
	print('北京欢迎你！')


# 无参数的函数调用
welcome_beijing()


# 带有参数的函数
# 注意PYCHARM软件中灰色的部分
def welcome_beijing_parameter(name):
	"""
	欢迎每一个人来到北京
	:param name: 表示旅行社的人名
	:return:
	"""
	print(f'{name}，北京欢迎你！')


# 带有参数的函数调用
welcome_beijing_parameter('小码哥')
welcome_beijing_parameter('刘德华')
welcome_beijing_parameter('杨幂')