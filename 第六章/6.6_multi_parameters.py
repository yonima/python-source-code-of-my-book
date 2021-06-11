# -*- coding: utf-8 -*-
"""
参数列表：多个参数  ---  形参列表 VS 实参列表
需求：
	刘德华, 北京欢迎你！你想去哪里玩？
	小码哥, 北京欢迎你！你在北京住几年了？
	杨幂, 北京欢迎你！你最喜欢北京什么？
"""


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


# 带有多个参数的函数
# 注意：没有调用测试灰色的
def welcome_beijing_more(name, question):
	"""
	实现询问顾客更多信息
	:param name: 记录人名
	:param question: 问题
	:return:
	"""
	print(f'{name},北京欢迎你！{question}')


# 带有参数的函数调用
'''
实现需求：
刘德华, 北京欢迎你！你想去哪里玩？
小码哥, 北京欢迎你！你在北京住几年了？
杨幂, 北京欢迎你！你最喜欢北京什么？
'''
welcome_beijing_more('刘德华', '你想去哪里玩？')
welcome_beijing_more('小码哥', '你在北京住几年了？')
welcome_beijing_more('杨幂', '你最喜欢北京什么？')
