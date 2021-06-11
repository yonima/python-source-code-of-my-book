# -*- coding: utf-8 -*-
"""
参数传递
"""


# 带有参数的函数
def welcome_beijing(name):
	print(f'{name}, 北京欢迎你！')


# 带有参数的函数调用
welcome_beijing('刘德华')
welcome_beijing('小码哥')
welcome_beijing('杨幂')

'''
参数列表
'''


# 带有多个参数的函数
# 注意：没有调用测试灰色的
def welcome_beijing(name, question):
	print(f'{name}, 北京欢迎你！{question}')

	
# 带有参数的函数调用
'''
实现需求：
刘德华, 北京欢迎你！你想去哪里玩？
小码哥, 北京欢迎你！你在北京住几年了？
杨幂, 北京欢迎你！你最喜欢北京什么？
'''
welcome_beijing('刘德华', '你想去哪里玩？')
welcome_beijing('小码哥', '你在北京住几年了？')
welcome_beijing('杨幂', '你最喜欢北京什么？')

# 互换实参的位置
print('互换实参的位置后的结果为：')
welcome_beijing('你想去哪里玩？', '刘德华')

# welcome_beijing('小码哥', '你在北京住几年了？')
# welcome_beijing('杨幂', '你最喜欢北京什么？')

# 缺少一个位置？
print('缺少一个位置参数的后果：')
welcome_beijing('你想去哪里玩？')