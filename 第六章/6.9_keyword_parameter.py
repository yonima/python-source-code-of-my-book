# -*- coding: utf-8 -*-
"""
关键字实参 -- 解决参数位置互换问题
需求：
刘德华, 北京欢迎你！你想去哪里玩？
小码哥, 北京欢迎你！你在北京住几年了？
杨幂, 北京欢迎你！你最喜欢北京什么？
"""


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


# 关键字实参
welcome_beijing(question= '你想去哪里玩？', name='刘德华')
# 练习 小码哥和杨幂

#  注意：关键字实参中的形参名字一定要正确
welcome_beijing(queston= '你想去哪里玩？', name='刘德华')