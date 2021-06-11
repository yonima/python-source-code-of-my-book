# -*- coding: utf-8 -*-
"""
参数的位置很重要：不能缺多，不能少，也不能互换

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

# 互换实参的位置
print('互换实参的位置后的结果为：')
welcome_beijing( '你想去哪里玩？','刘德华' )

# 作业-- 希望您能手互换一下，感受一下
welcome_beijing('小码哥', '你在北京住几年了？')
welcome_beijing('杨幂', '你最喜欢北京什么？')

# 缺少一个位置？
print('缺少一个位置参数的后果：')
print()
# welcome_beijing('小码哥')

# 多一个呢？
print('多一个参数！')
welcome_beijing('杨幂', '小码哥','你最喜欢北京什么？')